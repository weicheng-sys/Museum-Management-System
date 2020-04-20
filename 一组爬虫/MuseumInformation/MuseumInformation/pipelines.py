# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
class MuseuminformationPipeline(object):
    def __init__(self):
        self.fp = open("tableone.json",'w',encoding='utf-8')
    def open_spider(self, spider):
        print("爬虫开始")

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束")

import codecs
# class MuseuminformationPipeline(object):
#     def start_spider(self):
#         self.filename = codecs.open("museum-table/tableone.json", 'w', encoding='utf-8')
#         print("爬虫开始")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False) +'\n'
#         self.filename.write(item_json)
#         return item
#
#     def close_spider(self, spider):
#         self.filename.close()
#         print("爬虫结束")


# from scrapy.exporters import JsonItemExporter
# class MuseuminformationPipeline(object):
#     def __init__(self):
#         self.fp = open("tableone.json",'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print("爬虫开始")
#
#     def process_item(self, item, spider):
#         # item_json = json.dumps(dict(item), ensure_ascii=False)
#         # self.fp.write(item_json+'\n')
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束")


# from scrapy.exporters import JsonLinesItemExporter
# class MuseuminformationPipeline(object):
#     def __init__(self):
#         self.fp = open("tableone.json",'wb')
#         self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#
#     def open_spider(self, spider):
#         print("爬虫开始")
#
#     def process_item(self, item, spider):
#         # item_json = json.dumps(dict(item), ensure_ascii=False)
#         # self.fp.write(item_json+'\n')
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print("爬虫结束")




