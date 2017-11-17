# coding:utf-8
import urllib
import scrapy
import os
from tutorial.items import MeizituSpiderItem

#爬取http://www.mzitu.com/上的所有图片



all_page_link = [] #存储每个分类的路径
final_page_link=[] #存储每张图片的路径




class meizitu_spider(scrapy.Spider):


    name = 'meizitu'

    start_urls = ['http://www.mzitu.com/']
    
    allowed_domains = ['www.mzitu.com']
    
    def parse(self,response):
        print('------------开始---------')
        root_path = 'd:/meizitu'
        trantab = str.maketrans('\/:*?"<>|','abcdefghi')#这是针对WINDOWS下创建文件名可能存在的非法字符进行替换
        if response.url not in all_page_link:
            all_page_link.append(response.url)#做记录
            detail_page = scrapy.Selector(response).xpath('//ul[@id="pins"]/li/a/@href').extract()#当前页下所有分类url
            detail_name = scrapy.Selector(response).xpath('//ul[@id="pins"]/li/span/a/text()').extract()#当前页下所有分类名称
            for page,name in zip(detail_page,detail_name):#进行遍历
                name = name.translate(trantab)#替换非法字符
                dir_path = '%s/%s'%(root_path,name)
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)#找到每一分类的时候先创建目录，后续就不用创建了
                yield scrapy.Request(page,callback =self.pic_download)#每一页的每一分类转入下一函数进行处理
        next_url = scrapy.Selector(response).xpath('//a[@class="next page-numbers"]/@href').extract()[0]#下一页的地址
        yield scrapy.Request(next_url,callback =self.parse)#爬完当前页的所有分类，就进入下一页回调函数



    def pic_download(self,response):
        item = MeizituSpiderItem()
        pic_name= scrapy.Selector(response).xpath('//div[@class="main-image"]/p/a/img/@alt').extract()[0]
        trantab = str.maketrans('\/:*?"<>|','abcdefghi')
        item['pic_name']= pic_name.translate(trantab)#依然是替换非法字符，之前是为了创建目录，这里是为了把图片应存储的本地分类路劲写入到item中
        item['pic_url'] = scrapy.Selector(response).xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]#点进来的第一页的图片地址
        yield item#进入管道处理
        url_num = scrapy.Selector(response).xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').extract()[0]#找到该分类的页数
        for i in range(2,int(url_num)+1):#从第二页开始进行遍历
            link ='{}/{}'.format(response.url,i)
            if link not in final_page_link:
                final_page_link.append(link)#做记录
                yield scrapy.Request(link,callback = self.pic_download_next)#调用后续函数，这里不能回调该函数,原因看readme



    def pic_download_next(self,response):
        item = MeizituSpiderItem()
        pic_name= scrapy.Selector(response).xpath('//div[@class="main-image"]/p/a/img/@alt').extract()[0]
        trantab = str.maketrans('\/:*?"<>|','abcdefghi')#同上
        item['pic_name']= pic_name.translate(trantab)
        item['pic_url'] = scrapy.Selector(response).xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]
        yield item#进入管道处理

