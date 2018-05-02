# Python-Scrapy-Mzitu

使用scrapy对mzitu.com进行的全站图片爬取

### 爬取时间大概一个晚上，对比数量应该差不多全部爬取了，除了一些新添加的图片和由于网络问题导致的爬取失败
搞了很久的思路爬取，不是说多难，是有点犹豫使用哪一点，中途遇到一些坑，有空说吧<br>
思路：<br>
    处理每一个Page和每一个栏目分为两部分<br>
    处理Page:<br>
    第一页 =》获取3*8=24个栏目的地址 =》每一个栏目调用处理栏目<br>
    获取下一页回调这一步骤<br>
    处理栏目：<br>
    获取栏目总有多少页（有页码规律：/页数）<br>
    遍历每一页=》获取图片地址=》下载<br>

 ![1](https://github.com/Neocou/Python-Scrapy-Mzitu/blob/master/pic/1.PNG)

 ![2](https://github.com/Neocou/Python-Scrapy-Mzitu/blob/master/pic/2.PNG)
 
 ![3](https://github.com/Neocou/Python-Scrapy-Mzitu/blob/master/pic/3.PNG)<br>
 
 
 
 
 
 
## 十几个G百度云也放不上去，本来还想做个第一次爬全站的纪念。。。。。


