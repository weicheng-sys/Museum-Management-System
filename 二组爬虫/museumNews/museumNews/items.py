# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MuseumnewsItem(scrapy.Item):
    # 博物馆名
    museumName = scrapy.Field()

    # #新闻好坏
    evaluation = scrapy.Field()

    # 发布源
    source = scrapy.Field()

    # 新闻名称
    newsTitle = scrapy.Field()

    # 新闻内容
    newsContent = scrapy.Field()

    # 新闻图片
    newsPicture = scrapy.Field()

    # 发布时间
    publishTime = scrapy.Field()

    # 发布方
    publisher = scrapy.Field()
