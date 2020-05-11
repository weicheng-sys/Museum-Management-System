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
    # 博物馆编号
    mid = scrapy.Field()
    # 博物馆名称
    mname = scrapy.Field()
    # 图片
    mimg = scrapy.Field()
    # 评价
    evaluate = scrapy.Field()
    # 评分
    grade = scrapy.Field()
    # 基本信息
    basic_info = scrapy.Field()
    # 其他信息
    other_info = scrapy.Field()
    # museumPosition = scrapy.Field()
    # buildingType = scrapy.Field()
    # ticket = scrapy.Field()
    # buildingTime = scrapy.Field()
    # openingHours = scrapy.Field()
    # collectionNum = scrapy.Field()
    # collectionType = scrapy.Field()
    # number = scrapy.Field()
    # picture = scrapy.Field()
    # VideoAudio = scrapy.Field()
    # evaluate = scrapy.Field()
    # grade = scrapy.Field()



