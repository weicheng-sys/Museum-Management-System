# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymysql
import datetime
from dateutil.parser import parse
from analysis.analysis import analysis_content
import traceback

class Pipeline(object):
    def __init__(self):
        pass
        # self.con = pymysql.connect(host='rm-8vb178367o06xa531do.mysql.zhangbei.rds.aliyuncs.com',
        #                            user='passer',
        #                            password='xxxyJK1702',
        #                            database='museum_news',
        #                            charset='utf8')

    def process_item(self, item, spider):
        print(item)
        pass
        # if item['newsTitle'] is None or item['newsContent'] == "":
        #     pass
        # else:
        #     cursor = self.con.cursor()
        #     info = dict(item)
        #     try:
        #         sql = "insert into news (title, content, publisher, ntime, nimg," \
        #               "mname, evaluation, source) values (%s,%s,%s,%s,%s,%s,%s,%s);"
        #         cursor.execute(sql, [info['newsTitle'], info['newsContent'], info['publisher'], parse(info['publishTime']),
        #                              str(info['newsPicture']), info['museumName'], analysis_content(info["newsContent"]), info['source']])
        #         print(sql)
        #         self.con.commit()
        #     except Exception:
        #         traceback.print_exc()
        #         print(info['publishTime'])
        #         self.con.rollback()
        #     finally:
        #         cursor.close()



    def close_spider(self, spider):
        # self.con.close()
        print("关闭链接")
