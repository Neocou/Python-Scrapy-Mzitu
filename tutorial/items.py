# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MeizituSpiderItem(scrapy.Item):
	"""docstring for ClassName"""

	pic_url = scrapy.Field()
	pic_name = scrapy.Field()
		