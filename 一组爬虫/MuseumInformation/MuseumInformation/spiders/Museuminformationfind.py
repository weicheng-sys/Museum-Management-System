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

            if i==11:
                yield scrapy.Request(url, callback=lambda response, num=i: self.parse11(response, num))  # 调用爬虫程序
            elif i==54:
                yield scrapy.Request(url, callback=lambda response, num=i: self.parse54(response, num))  # 调用爬虫程序
            elif i==74:
                yield scrapy.Request(url, callback=lambda response, num=i: self.parse74(response, num))  # 调用爬虫程序
            elif i==38:
                yield scrapy.Request(url, callback=lambda response, num=i: self.parse38(response, num))  # 调用爬虫程序
            elif i==46:
                yield scrapy.Request(url, callback=lambda response, num=i: self.parse46(response, num))  # 调用爬虫程序
            elif i == 84:
                yield scrapy.Request(url, callback=lambda response, num=i: self.parse46(response, num))  # 调用爬虫程序
            else:
                yield scrapy.Request(url, callback=lambda response , num=i: self.parse1(response, num))  #调用爬虫程序

            i += 1

    def parse1(self, response,i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)


        # statics = response.xpath("//div[@class='basic-info cmn-clearfix']")
        # key = []
        # nvalue = []
        # for value in statics:
        #     # Selector，正则表达式
        #     key = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
        #     key[0] = '博物馆名称'
        #     # print(key)
        #     nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
        #     # print(nvalue)
        # i = 0
        # while i < len(nvalue):
        #     nvalue[i] = nvalue[i].replace('\n', '')
        #     i += 1

        # 博物馆名
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
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i <len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            tt = t.replace('：', '')
            key.append(tt)
            print(tt)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"','')
            print(ttt)
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)


        # 其他信息
        other_info = []
        statics = response.xpath("//div[@class='lemma-summary']")
        # 简介
        # statics = response.xpath("/div[@class='para']")

        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()
            value = re.sub('[\d]]','',"".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            tt = t.replace('/','')
            ttt = tt.replace('xa0"', '')
            tttt = ttt.replace('\"', '')

            value = tttt.replace(" -", '')

            other_info.append(value)


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
        # print(item)

        yield item

    def parse11(self, response, i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)


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
                del (mimg[j])
                j -= 1
            j += 1
        # print(ming)

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # 基本信息
        basic_info = []
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i < len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            key.append(t)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"', '')
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)

        # 其他信息
        other_info = []
        temp = []
        statics = response.xpath("//div[@class='lemma-summary']/div[@class='para']")
        # 简介
        other_info.append("简介")
        # statics = response.xpath("/div[@class='para']")
        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()
            # value = value.replace('\n', '')
            value = "".join(value)
            t = value.replace('[', '')
            tt = t.replace('/', '')
            value = tt.replace(" -", '')
            temp.append(value)

        other_info.append(temp)

        # 标题
        statics = response.xpath("//div[@class='para']")


        other_info.append("建筑布局")
        temp = []
        j = 23
        while j < 28:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            tt = t.replace('/', '')
            value = tt.replace(" -", '')
            temp.append(value)
            j += 1
        temp.extend(["|"])
        other_info.append("".join(temp))

        other_info.append("馆藏精品")
        temp = []
        j = 30
        while j <60:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            tt = t.replace('/', '')
            value = tt.replace(" -", '')
            temp.append(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("展厅介绍")
        temp = []
        j = 62
        while j < 152:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            tt = t.replace('/', '')
            value = tt.replace(" -", '')
            temp.append(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)


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

        yield item

    def parse38(self, response, i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)

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
                del (mimg[j])
                j -= 1
            j += 1
        # print(ming)

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # 基本信息
        basic_info = []
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i < len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            key.append(t)
            print(t)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"', '')
            print(ttt)
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)

        # 其他信息
        other_info = []
        temp = []
        statics = response.xpath("//div[@class='lemma-summary']/div[@class='para']")
        # 简介
        other_info.append("简介")

        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()
            # value = value.replace('\n', '')
            temp.extend(value)

        other_info.append(temp)

        statics = response.xpath("//div[@class='para']")
        # 标题
        other_info.append("历史沿革")
        temp = []
        j = 3
        while j < 18:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("馆藏精品")
        temp = []
        j = 19
        while j < 29:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("展厅陈列")
        temp = []
        j = 29
        while j < 50:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("科研文化")
        temp = []
        j = 88
        while j < 96:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

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

        yield item

    def parse46(self, response, i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)

        statics = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']")
        for value in statics:
            mname = value.xpath(".//h1//text()").getall()
        mname = mname[0]

        # 图片
        pics0 = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        pics1 = response.xpath('//div[@class="album-wrap"]//img/@src').extract()
        pics2 = response.xpath(
            '//div[@class="lemma-picture text-pic layout-center"]//img/@src').extract()
        pics3 = response.xpath(
            '//div[@class="lemma-picture text-pic layout-right"]//img/@src').extract()
        pics4 = response.xpath('//div[@class="lemma-picture text-pic layout-left"]//img/@src').extract()
        mimg = pics0 + pics1 + pics2 + pics3 + pics4
        j = 0
        while j < len(mimg):
            if "https://" not in mimg[j]:
                del (mimg[j])
                j -= 1
            j += 1
        # print(ming)

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # 基本信息
        basic_info = []
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i < len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            key.append(t)
            print(t)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"', '')
            print(ttt)
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)

        # 其他信息
        other_info = []
        temp = []
        statics = response.xpath("//div[@class='lemma-summary']/div[@class='para']")
        # 简介
        other_info.append("简介")
        # statics = response.xpath("/div[@class='para']")
        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()
            # value = value.replace('\n', '')
            temp.extend(value)

        other_info.append(temp)

        # 标题
        statics = response.xpath("//div[@class='para']")
        print(statics)

        other_info.append("建筑特色")
        temp = []
        j = 3
        while j < 6:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("展厅分布")
        temp = []
        j = 6
        while j < 12:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("馆藏文物")
        temp = []
        j = 12
        while j < 20:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("机构文化")
        temp = []
        j = 107
        while j < 109:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("价值")
        temp = []
        j = 109
        while j < 111:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            temp.extend(value)
            j += 1
        temp.extend(["|"])
        other_info.append(temp)

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

        yield item

    def parse54(self, response,i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)


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
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i < len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            key.append(t)
            print(t)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"', '')
            print(ttt)
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)
        # 其他信息
        other_info = []
        temp = []
        statics = response.xpath("//div[@class='lemma-summary']/div[@class='para']")
        # 简介
        other_info.append("简介")
        #statics = response.xpath("/div[@class='para']")
        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)

        other_info.append(temp)
        # 标题
        other_info.append("发展历史")
        statics = response.xpath("//div[@class='para']")
        temp = []
        j = 4
        while j < 8:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        other_info.append(temp)

        other_info.append("主要展馆")
        # ttstatics = response.xpath("//div[@class='para-title level-3']/h3")
        # tt = ttstatics.xpath('string(.)').extract()
        temp = []
        temp.extend(["南馆"])
        value = statics[8].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)
        temp.extend(["|"])

        temp.extend(["北馆"])
        j = 9
        while j < 17:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        temp.extend(["机动展厅"])
        value = statics[17].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)
        temp.extend(["|"])
        other_info.append(temp)

        other_info.append("馆藏文物")
        temp = []
        temp.extend(["综述"])
        value = statics[18].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)
        temp.extend(["|"])

        temp.extend(["精品"])
        j = 21
        while j < 43:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        other_info.append(temp)


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

        yield item

    def parse74(self, response,i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)



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
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i < len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            key.append(t)
            print(t)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"', '')
            print(ttt)
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)

        # 其他信息
        other_info = []
        temp = []
        intab = r"\n[]"
        outtab = "    "
        trantab = str.maketrans(intab, outtab)
        statics = response.xpath("//div[@class='lemma-summary']/div[@class='para']")
        # 简介
        other_info.append("简介")
        #statics = response.xpath("/div[@class='para']")
        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)

        other_info.append(temp)
        # 标题
        # other_info.append("建筑布局")
        statics = response.xpath("//div[@class='para']")
        # temp = []
        # value = statics[24].xpath('normalize-space(string(.))').extract()
        #
        # value = re.sub('[\d]]', '', "".join(value))
        # value = re.sub('[\d]', '', "".join(value))
        # t = value.replace('[', '')
        # value = t.replace(" -", '')
        #
        #
        # temp.extend(value)
        # other_info.append(temp)

        other_info.append("馆藏精品")
        # ttstatics = response.xpath("//div[@class='para-title level-3']/h3")
        # tt = ttstatics.xpath('string(.)').extract()
        temp = []
        # temp.extend(["莲鹤方壶"])
        # j = 28
        # while j < 32:
        #     value = statics[j].xpath('normalize-space(string(.))').extract()
        #
        #     value = re.sub('[\d]]', '', "".join(value))
        #     value = re.sub('[\d]', '', "".join(value))
        #     t = value.replace('[', '')
        #     value = t.replace(" -", '')
        #
        #     temp.extend(value)
        #     j += 1
        # temp.extend(["|"])
        #
        # temp.extend(["妇好鸮尊"])
        # j = 32
        # while j < 37:
        #     value = statics[j].xpath('normalize-space(string(.))').extract()
        #
        #     value = re.sub('[\d]]', '', "".join(value))
        #     value = re.sub('[\d]', '', "".join(value))
        #     t = value.replace('[', '')
        #     value = t.replace(" -", '')
        #
        #     temp.extend(value)
        #     j += 1
        # temp.extend(["|"])
        #
        # temp.extend(["杜岭方鼎"])
        # j = 37
        # while j < 40:
        #     value = statics[j].xpath('normalize-space(string(.))').extract()
        #
        #     value = re.sub('[\d]]', '', "".join(value))
        #     value = re.sub('[\d]', '', "".join(value))
        #     t = value.replace('[', '')
        #     value = t.replace(" -", '')
        #
        #     temp.extend(value)
        #     j += 1
        # temp.extend(["|"])
        #
        # temp.extend(["云纹铜禁"])
        # j = 40
        # while j < 44:
        #     value = statics[j].xpath('normalize-space(string(.))').extract()
        #
        #     value = re.sub('[\d]]', '', "".join(value))
        #     value = re.sub('[\d]', '', "".join(value))
        #     t = value.replace('[', '')
        #     value = t.replace(" -", '')
        #
        #     temp.extend(value)
        #     j += 1
        # temp.extend(["|"])

        temp.extend(["武曌金简"])
        j = 44
        while j < 49:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        temp.extend(["玉柄铁剑"])
        j = 49
        while j < 54:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        temp.extend(["贾湖骨笛"])
        j = 54
        while j < 57:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        temp.extend(["四神云气图"])
        j = 57
        while j < 62:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        other_info.append(temp)


        other_info.append("展厅介绍")
        temp=[]
        value = statics[62].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)

        temp.extend(["古代文明之光"])
        value = statics[65].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)
        temp.extend(["|"])

        temp.extend(["青铜艺术馆"])
        j = 68
        while j < 70:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        temp.extend(["古代玉器馆"])
        value = statics[71].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)
        temp.extend(["|"])

        temp.extend(["明清珍宝馆"])
        value = statics[73].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')

        temp.extend(value)
        temp.extend(["|"])

        other_info.append(temp)


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

        yield item

    def parse84(self, response,i):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName

        # 博物馆编号
        i = list(str(i))
        while len(i) < 3:
            i.insert(0, '0')
        mid = "".join(i)
        print(mid)



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
        nvalues = response.xpath("//dt[@class='basicInfo-item name']/text()").extract()
        print(nvalues)
        vvalues = response.xpath("//dd[@class='basicInfo-item value']")
        vvalues = vvalues.xpath('string(.)').extract()
        print(vvalues)

        key = []
        val = []
        i = 0
        while i < len(nvalues):
            t = nvalues[i].replace('\xa0', '')
            key.append(t)
            print(t)
            i += 1
        i = 0
        while i < len(vvalues):
            t = vvalues[i].replace('\n', '')
            tt = t.replace('\xa0', '')
            ttt = tt.replace('\"', '')
            print(ttt)
            val.append(ttt)
            i += 1

        for i, j in zip(key, val):
            basic_info.append(i)
            basic_info.append(j)

        # 其他信息
        other_info = []
        temp = []
        statics = response.xpath("//div[@class='lemma-summary']/div[@class='para']")
        intab = r"\n[]"
        outtab = "    "
        trantab = str.maketrans(intab, outtab)
        # 简介
        other_info.append("简介")
        #statics = response.xpath("/div[@class='para']")
        for value in statics:
            value = value.xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)

        other_info.append(temp)
        # 标题
        other_info.append("建筑布局")
        statics = response.xpath("//div[@class='para']")
        temp = []
        j = 24
        while j < 26:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        other_info.append(temp)

        other_info.append("展览")
        temp = []
        j = 26
        while j < 45:
            value = statics[j].xpath('normalize-space(string(.))').extract()

            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        other_info.append(temp)


        other_info.append("馆藏文物")
        temp = []
        temp.extend(["综述"])
        value = statics[48].xpath('normalize-space(string(.))').extract()

        value = re.sub('[\d]]', '', "".join(value))
        value = re.sub('[\d]', '', "".join(value))
        t = value.replace('[', '')
        value = t.replace(" -", '')


        temp.extend(value)
        temp.extend(["|"])

        temp.extend(["馆藏精品"])
        j = 49
        while j < 121:
            value = statics[j].xpath('normalize-space(string(.))').extract()
            value = re.sub('[\d]]', '', "".join(value))
            value = re.sub('[\d]', '', "".join(value))
            t = value.replace('[', '')
            value = t.replace(" -", '')

            temp.extend(value)
            j += 1
        temp.extend(["|"])

        other_info.append(temp)


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

        yield item