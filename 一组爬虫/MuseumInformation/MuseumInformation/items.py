# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MuseuminformationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 表一
    museumId = scrapy.Field()
    museumName = scrapy.Field()
    museumPosition = scrapy.Field()
    buildingType = scrapy.Field()
    ticket = scrapy.Field()
    buildingTime = scrapy.Field()
    openingHours = scrapy.Field()
    collectionNum = scrapy.Field()
    collectionType = scrapy.Field()
    number = scrapy.Field()
    picture = scrapy.Field()
    VideoAudio = scrapy.Field()
    evaluate = scrapy.Field()
    grade = scrapy.Field()



