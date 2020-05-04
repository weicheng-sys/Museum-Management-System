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

# 导入库
from scrapy.utils.project import get_project_settings
import pymysql

# 写入数据库
class MySQLPipeline(object):
    def connect_db(self):
        # 从settings.py文件中导入数据库连接需要的相关信息
        settings = get_project_settings()

        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        # 连接数据库
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.name,  # 数据库名
            charset = self.charset,
        )

        # 操作数据库的对象
        self.cursor = self.conn.cursor()

    # 连接数据库
    def open_spider(self, spider):
        self.connect_db()

    # 关闭数据库连接
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    # 写入数据库
    def process_item(self, item, spider):
        # 写入数据库内容
        # 这里根据需求自行设置要写入的字段及值
        sql = 'insert into museum (mid,mname,mimg,evaluate,grade,basic_info, other_info) values ("%s", "%s", "%s","%s", "%s", "%s","%s")' % (item['mid'],item['mname'], item['mimg'], item['evaluate'], item['grade'],item['basic_info'],item['other_info'])
        #, basic_info, other_info
        #, item['basic_info'], item['other_info']
        # 执行sql语句
        self.cursor.execute(sql)

        # 需要强制提交数据，否则数据回滚之后，数据库为空
        self.conn.commit()

        return item

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




