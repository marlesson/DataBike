# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Station(scrapy.Item):
    # define the fields for your item here like:
    name  = scrapy.Field()
    address = scrapy.Field()
    lat   = scrapy.Field()
    lng   = scrapy.Field()
    status = scrapy.Field()
    available = scrapy.Field()
    free  = scrapy.Field()
    created_at = scrapy.Field()

    source = scrapy.Field()

