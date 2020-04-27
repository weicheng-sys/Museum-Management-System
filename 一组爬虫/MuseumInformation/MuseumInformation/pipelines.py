# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from MuseumInformation.items import MuseuminformationItem
class MuseuminformationPipeline(object):
    def __init__(self):
        self.fp = open("tableone.json",'w',encoding='utf-8')
    def open_spider(self, spider):
        print("爬虫开始")
        # self.config = pymysql.connect(
        #     host='127.0.0.1',
        #     # port=3306,
        #     user='museum',
        #     port=3306,
        #     passwd='Museum123',
        #     db='db',
        #     charset='utf8')
        # self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item
        # insert_sql = "INSERT INTO hx(mid, mname, ming, evaluate, grade, basic_info, other_info) VALUES (%d, %s, %s, %s, %s, %s, %s)"
        # self.cursor.execute(insert_sql, (item['mid'], item['mname'], item['ming'], item['evaluate'], item['grade'], item['basic_info'], item['other_info']))
        # self.client.commit()


    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束")
        # self.cursor.close()
        # self.connect.close()



#
# # 连接配置信息
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'museum',
#     'password': 'Museum123',
#     'db': 'db',
#     'charset': 'utf8',
#     'cursorclass': pymysql.cursors.DictCursor,
# }
#
# # 创建连接
# connection = pymysql.connect(**config)
# # # 创建游标方法1
# # cursor = connection.cursor()
# # 创建游标方法2 取别名为 cursor
# with connection.cursor() as cursor:
#     # # 执行sql语句，插入记录
#     # sql = 'INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
#     # cursor.execute(sql, ('Robin', 'Zhyea', tomorrow, 'M', date(1989, 6, 14)))  # 插入一条数据
#     # data为多条数据，放在一个元组或者列表中
#     cursor.executemany(sql, data)  # 插入多条数据
# # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
# connection.commit()  # 连接提交事务
# cursor.close()  # 关闭游标连接
# connection.close();  # 关闭连接，释放内存

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




