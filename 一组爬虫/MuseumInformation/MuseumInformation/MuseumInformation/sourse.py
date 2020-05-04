#-*- codeing = utf-8 -*-
import xlrd
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request,urllib.error # 制定URL，后去网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import pymysql
import openpyxl
from openpyxl import load_workbook
def getexcel():
    # 打开文件
    web = str(r'博物馆链接总表 .xlsx')
    sheet = xlrd.open_workbook(web)
    table = sheet.sheet_by_name('Sheet1')
    # 查询工作表
    sourse = []  # 存储从表里拿出来的数据
    # 第一列的 0-25 个数据
    for i in range(52, 78):
        sourse.append(table.cell(i, 0).value)  # i——行，0——列
    print(sourse)
    return sourse
