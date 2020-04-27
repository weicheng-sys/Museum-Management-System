# -*- coding: utf-8 -*-
import scrapy
import json
from bs4 import BeautifulSoup  # 网页解析，获取数据
import xlrd
from urllib.parse import unquote
from MuseumInformation.items import MuseuminformationItem
import re  # 正则表达式，进行文字匹配
# from MuseumInformation1.sourse import getexcel
# response = HtmlResponse

class MuseuminformationFind(scrapy.Spider):  #必须继承spider类
    name = 'museum'
    allowed_domains = ['baike.baidu.com']  #限制范围在百度百科
    start_urls = ['https://baike.baidu.com/item/国家一级博物馆/1372604?fr=aladdin']



    # 爬取全国130个一级博物馆的链接
    def parse(self, response):
        sourse = []
        slinks = response.xpath("//table")
        link = slinks.xpath(".//tr/td[@align='center']//a/@href").extract()
        add = "https://baike.baidu.com"
        for item in link:
            linkitem = add + item
            sourse.append(linkitem)
        sourse.append("https://baike.baidu.com/item/%E5%A4%A7%E8%BF%9E%E7%8E%B0%E4%BB%A3%E5%8D%9A%E7%89%A9%E9%A6%86/10876521?fr=aladdin")
        sourse.append("https://baike.baidu.com/item/%E6%AD%A6%E6%B1%89%E4%B8%AD%E5%B1%B1%E8%88%B0%E5%8D%9A%E7%89%A9%E9%A6%86/692909?fromtitle=%E6%AD%A6%E6%B1%89%E5%B8%82%E4%B8%AD%E5%B1%B1%E8%88%B0%E5%8D%9A%E7%89%A9%E9%A6%86&fromid=23692987&fr=aladdin")
        sourse[44] = "https://baike.baidu.com/item/南通博物苑/1629642"
        sourse[74] = "https://baike.baidu.com/item/%E9%83%91%E5%B7%9E%E5%8D%9A%E7%89%A9%E9%A6%86/783622"
        sourse[101] = "https://baike.baidu.com/item/四川博物院/2812558"
        i = 1
        for url in sourse:
            yield scrapy.Request(url, callback=lambda response , num=i: self.parse1(response, num))  #调用爬虫程序
            i += 1
        # # 排序
        # f = open('tableone.json','w')
        # # 将json格式的数据映射成list的形式
        # t = json.load(f)

    def parse1(self, response,i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)


        statics = response.xpath("//div[@class='basic-info cmn-clearfix']")
        key = []
        nvalue = []
        for value in statics:
            # Selector，正则表达式
            key = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            key[0] = '博物馆名称'
            print(key)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            print(nvalue)
        i = 0
        while i < len(nvalue):
            nvalue[i] = nvalue[i].replace('\n', '')
            i += 1
        statics = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']")
        for value in statics:
            mname = value.xpath(".//h1//text()").getall()
        mname = mname[0]

        # 图片
        pics0 = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        pics1 = response.xpath('//div[@class="album-wrap"]//img/@src').extract()
        pics2 = response.xpath('//div[@class="lemma-picture text-pic layout-center"]//img/@src').extract()
        pics3 = response.xpath('//div[@class="lemma-picture text-pic layout-right"]//img/@src').extract()
        pics4 = response.xpath('//div[@class="lemma-picture text-pic layout-left"]//img/@src').extract()
        mimg = pics0 + pics1 + pics2 + pics3 + pics4
        j = 0
        while j < len(mimg):
            if "https://" not in mimg[j]:
                del(mimg[j])
                j -= 1
            j += 1
        # print(ming)

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # 基本信息
        basic_info = []
        # basic_info.append(key)
        # basic_info.append(value)
        # basic_info = key + nvalue
        for i, j in zip(key, nvalue):
            basic_info.append(i)
            basic_info.append(j)

        # 其他信息
        other_info = []
        statics = response.xpath("//div[@class='para-title level-2']")
        # 标题
        for value in statics:
            # Selector，正则表达式
            key = value.xpath(".//h2[@class='title-text']//text()").getall()
            key = key[1]
            # print(key)
        # 信息
        statics = response.xpath("//div[@class='para']")
        for value in statics:
            value = value.xpath('string(.)').extract()
            # value = value.replace('\n', '')
            other_info.append(value)
        # 问题，无法对应

        zkey = ['mid', 'mname', 'mimg', 'evaluate', 'grade', 'basic_info', 'other_info']
        # zvalue = mid + mname + mimg + evaluate + grade + basic_info + other_info
        zvalue = []
        zvalue.append(mid)
        zvalue.append(mname)
        zvalue.append(mimg)
        zvalue.append(evaluate)
        zvalue.append(grade)
        zvalue.append(basic_info)
        zvalue.append(other_info)


        item = dict(zip(zkey, zvalue))
        print(item)
        # # 排序
        # sorted(item.items(),key=lambda  item:item[0],reverse=False)
        # print(item)
        # item = MuseuminformationItem(mid=mid,mname=mname, mimg=mimg,
        #                              evaluate=evaluate, grade=grade,
        #                              basic_info=basic_info, other_info=other_info)
        # yield item
        yield item
