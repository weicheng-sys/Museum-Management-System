# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class MuseumnewsPipeline(object):
    def start_spider(self):
        self.filename = codecs.open("museum_news/news_info.json", "w", encoding="utf-8")
        print("开启管道")

    def process_item(self, item, spider):
        if item['title'] is None or item['content'] == "":
            pass
        else:
            jsontext = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.filename.write(jsontext)
        return item

    def close_spider(self, spider):
        self.filename.close()
        print("关闭文件")