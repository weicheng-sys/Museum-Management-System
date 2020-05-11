# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 导入库
from scrapy.utils.project import get_project_settings
import pymysql

# 写入数据库
class MySQLPipeline(object):
    def __init__(self):
        self.con = pymysql.connect(host='rm-8vb178367o06xa531do.mysql.zhangbei.rds.aliyuncs.com',
                                   user='passer',
                                   password='xxxyJK1702',
                                   database='museum_news',
                                   charset='utf8')
        self.cursor = self.con.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.con.close()
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
        self.con.commit()
        return item
