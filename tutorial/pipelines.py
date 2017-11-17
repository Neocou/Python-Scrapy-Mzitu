# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import urllib
from urllib import request
from tutorial import settings



class MeizituPipeline(object):
    def process_item(self, item, spider):
        print('---------开始下载了-----------')
        pic_url = item['pic_url']
        name = pic_url.rsplit('/',1)[-1]#从url取图片名称
        root_path = 'd:/meizitu'
        dir_path = item['pic_name']#取出该图片应属于哪个分类
        file_path = '%s/%s/%s' %(root_path,dir_path,name)#拼接名称确认图片路径
        if not os.path.exists(file_path):#判断是否下载过
            print('%s下载'%(file_path))
            with open(file_path,'wb') as jpg:
                jpg.write(requests.get(pic_url,timeout = 15,headers=self.getheader(pic_url)).content)
        return item
        

    def getheader(self,refers):#要使用Referer指向，不然会被防盗链
        headers = DEFAULT_REQUEST_HEADERS = {
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Referer':'{}'.format(refers),
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
            }
        return headers

    def close_spider(self,spider):
        print('任务结束了！！！')#结束标识