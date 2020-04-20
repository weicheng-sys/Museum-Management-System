# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup  # 网页解析，获取数据
import xlrd
from urllib.parse import unquote
from MuseumInformation.items import MuseuminformationItem
import re  # 正则表达式，进行文字匹配
# from MuseumInformation1.sourse import getexcel
# response = HtmlResponse

class MuseuminformationFind(scrapy.Spider):
    name = 'museum'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/国家一级博物馆/1372604?fr=aladdin']

    # web = str(r'D:\python_code\MuseumInformation\MuseumInformation\spiders\博物馆链接总表.xlsx')
    # sheet = xlrd.open_workbook(web)
    # table = sheet.sheet_by_name('Sheet1')
    # # 查询工作表
    # sourse = []  # 存储从表里拿出来的数据
    # # 第一列的 0-25 个数据
    # for i in range(0, 130):
    #     sourse.append(table.cell(i, 0).value)  # i——行，0——列
    #
    # print(sourse)
    # start_urls = sourse[0]


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
        sourse[74] = "https://baike.baidu.com/item/%E9%83%91%E5%B7%9E%E5%8D%9A%E7%89%A9%E9%A6%86/783622"



        yield scrapy.Request(sourse[26], callback=self.parse27)
        yield scrapy.Request(sourse[27], callback=self.parse28)
        yield scrapy.Request(sourse[28], callback=self.parse29)
        yield scrapy.Request(sourse[29], callback=self.parse30)
        yield scrapy.Request(sourse[30], callback=self.parse31)
        yield scrapy.Request(sourse[31], callback=self.parse32)
        yield scrapy.Request(sourse[32], callback=self.parse33)
        yield scrapy.Request(sourse[33], callback=self.parse34)
        yield scrapy.Request(sourse[34], callback=self.parse35)
        yield scrapy.Request(sourse[35], callback=self.parse36)
        yield scrapy.Request(sourse[36], callback=self.parse37)
        yield scrapy.Request(sourse[37], callback=self.parse38)
        yield scrapy.Request(sourse[38], callback=self.parse39)
        yield scrapy.Request(sourse[39], callback=self.parse40)
        yield scrapy.Request(sourse[40], callback=self.parse41)
        yield scrapy.Request(sourse[41], callback=self.parse42)
        yield scrapy.Request(sourse[42], callback=self.parse43)
        yield scrapy.Request(sourse[43], callback=self.parse44)
        yield scrapy.Request(sourse[44], callback=self.parse45)
        yield scrapy.Request(sourse[45], callback=self.parse46)
        yield scrapy.Request(sourse[46], callback=self.parse47)
        yield scrapy.Request(sourse[47], callback=self.parse48)
        yield scrapy.Request(sourse[48], callback=self.parse49)
        yield scrapy.Request(sourse[49], callback=self.parse50)
        yield scrapy.Request(sourse[50], callback=self.parse51)
        yield scrapy.Request(sourse[51], callback=self.parse52)

        yield scrapy.Request(sourse[52], callback=self.parse53)
        yield scrapy.Request(sourse[53], callback=self.parse54)
        yield scrapy.Request(sourse[54], callback=self.parse55)
        yield scrapy.Request(sourse[55], callback=self.parse56)
        yield scrapy.Request(sourse[56], callback=self.parse57)
        yield scrapy.Request(sourse[57], callback=self.parse58)
        yield scrapy.Request(sourse[58], callback=self.parse59)
        yield scrapy.Request(sourse[59], callback=self.parse60)
        yield scrapy.Request(sourse[60], callback=self.parse61)
        yield scrapy.Request(sourse[61], callback=self.parse62)
        yield scrapy.Request(sourse[62], callback=self.parse63)
        yield scrapy.Request(sourse[63], callback=self.parse64)
        yield scrapy.Request(sourse[64], callback=self.parse65)
        yield scrapy.Request(sourse[65], callback=self.parse66)
        yield scrapy.Request(sourse[66], callback=self.parse67)
        yield scrapy.Request(sourse[67], callback=self.parse68)
        yield scrapy.Request(sourse[68], callback=self.parse69)
        yield scrapy.Request(sourse[69], callback=self.parse70)
        yield scrapy.Request(sourse[70], callback=self.parse71)
        yield scrapy.Request(sourse[71], callback=self.parse72)
        yield scrapy.Request(sourse[72], callback=self.parse73)
        yield scrapy.Request(sourse[73], callback=self.parse74)
        yield scrapy.Request(sourse[74], callback=self.parse75)
        yield scrapy.Request(sourse[75], callback=self.parse76)
        yield scrapy.Request(sourse[76], callback=self.parse77)
        yield scrapy.Request(sourse[77], callback=self.parse78)

        yield scrapy.Request(sourse[104], callback=self.parse105)
        yield scrapy.Request(sourse[105], callback=self.parse106)
        yield scrapy.Request(sourse[106], callback=self.parse107)
        yield scrapy.Request(sourse[107], callback=self.parse108)
        yield scrapy.Request(sourse[108], callback=self.parse109)
        yield scrapy.Request(sourse[109], callback=self.parse110)
        yield scrapy.Request(sourse[110], callback=self.parse111)
        yield scrapy.Request(sourse[111], callback=self.parse112)
        yield scrapy.Request(sourse[112], callback=self.parse113)
        yield scrapy.Request(sourse[113], callback=self.parse114)
        yield scrapy.Request(sourse[114], callback=self.parse115)
        yield scrapy.Request(sourse[115], callback=self.parse116)
        yield scrapy.Request(sourse[116], callback=self.parse117)
        yield scrapy.Request(sourse[117], callback=self.parse118)
        yield scrapy.Request(sourse[118], callback=self.parse119)
        yield scrapy.Request(sourse[119], callback=self.parse120)
        yield scrapy.Request(sourse[120], callback=self.parse121)
        yield scrapy.Request(sourse[121], callback=self.parse122)
        yield scrapy.Request(sourse[122], callback=self.parse123)
        yield scrapy.Request(sourse[123], callback=self.parse124)
        yield scrapy.Request(sourse[124], callback=self.parse125)
        yield scrapy.Request(sourse[125], callback=self.parse126)
        yield scrapy.Request(sourse[126], callback=self.parse127)
        yield scrapy.Request(sourse[127], callback=self.parse128)
        yield scrapy.Request(sourse[128], callback=self.parse129)
        yield scrapy.Request(sourse[129], callback=self.parse130)

    def parse105(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(105))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "票\xa0\xa0\xa0\xa0价":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "2000多件"

        # 藏品种类  collectionType
        collectionType = "革命文物及历史资料"

        # 展区数量  number
        number = "11个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse106(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(106))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0址":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1

        # 开放时间  openingHours
        openingHours = "NULL"
        # 藏品数量  collectionNum
        collectionNum = "20余万件"

        # 藏品种类  collectionType
        collectionType = "青铜器、古钱币、陶瓷器、古书画、碑贴、邮票及各类工艺品"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]
        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse107(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(107))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "昆明市滇池路1503号"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "票价为每人10元，对未成年人、中小学生、离休干部、现役军人、残疾人、劳模凭证免票。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "正常开放时间为每周二至周日上午9时至下午5时（周一休息）"

        # 藏品数量  collectionNum
        collectionNum = "12万件"

        # 藏品种类  collectionType
        collectionType = "民族古籍、文化遗产、民族服饰、民间美术、民族乐器、传统生产生活技术等"

        # 展区数量  number
        number = "16个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse108(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(108))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "9：00——17：00（周一闭馆）"

        # 藏品数量  collectionNum
        collectionNum = "馆藏文物约10万多件，资料5万多件"

        # 藏品种类  collectionType
        collectionType = "四川旧石器 500多件，巴蜀文物1000余件，汉画像石、画像砖100多件，历代名窑陶瓷器4000多件，宋元以来名家书画5000多件"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse109(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(109))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门\xa0\xa0\xa0\xa0票":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = "全年开放" + " " + nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "超过10万件"

        # 藏品种类  collectionType
        collectionType = "一级文物227件、二级文物284件、三级文物2749件"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse110(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(110))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "旧馆位于重庆市枇杷山正街74号，新馆位于重庆市北碚区金华路398号"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "11万余件"

        # 藏品种类  collectionType
        collectionType = "涵盖动物、植物、古生物、古人类、旧石器、地质矿产、岩石、土壤等八大学科"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse111(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(111))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "拉萨市罗布林卡东南角"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "夏季：10:00～17:30 冬季：10:00～16:30（周一不能参观）"

        # 藏品数量  collectionNum
        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "各种类型的史前文化遗物、多种质地和造型的佛、菩萨人物造像，历代蘸金粉、银粉、珊瑚粉等手写的藏文典籍，历代中央政府颁给大活佛的金印，金瓶掣签仪式使用的金瓶和玉签，五彩纷呈的唐卡画，各种乐器、法器，具有鲜明的民族特色的手工艺品，别有风格的陶器等等"

        # 展区数量  number
        number = "9个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse112(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(112))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省西安市雁塔区小寨东路91号"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费，凭有效证件换票参观"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "周二至周日全天开放"

        # 藏品数量  collectionNum
        i = 0
        while i < len(names):
            if names[i] == "馆藏文物数量":
                collectionNum = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品种类  collectionType
        collectionType = "馆藏文物上起远古人类初始阶段使用的简单石器，下至1840年前社会生活中的各类器物，时间跨度长达一百多万年"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse113(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(113))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省西安市临潼区秦陵镇"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "120元人民币/人次，学生证享半价优惠 ；65岁以上老人、残疾人、中国现役军人（含武警）、军队院校学员、退伍老红军战士、革命伤残军人、由家长携带的16岁以下未成年人免费。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        i = 0
        while i < len(names):
            if names[i] == "藏品数量":
                collectionNum = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品种类  collectionType
        collectionType = "陶俑、陶马、青铜兵器、铜车马"

        # 展区数量  number
        number = "4个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse114(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(114))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省延安市宝塔区王家坪路"

        # 博物馆类别  buildingType
        buildingType = "革命纪念博物馆"

        # 门票  ticket
        ticket = "免费，需携带身份证。"

        # 建馆时间  buildingTime
        buildingTime = "1950年7月"

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "文物有3.5万多件，历史照片5500多张，图书资料1.2万余册"

        # 藏品种类  collectionType
        collectionType = "一、二级文物有1700余件，延安时期出版发行的报刊杂志100余种。"

        # 展区数量  number
        number = "6个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse115(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(115))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省西安市北郊的渭河之畔"

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "旺季70.00元 淡季55.00元"

        # 建馆时间  buildingTime
        buildingTime = "1999年9月30日"

        # 开放时间  openingHours

        openingHours = "3－11月 8：30－19：00， 1月、2月和12月8：30－18：00"

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse116(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(116))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "展馆名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "西安市文昌门内三学街15号"

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "淡季（12月1日——次年2月底）全票50元/人，半票25元/人，旺季（3月1日——11月底）65元/人，半票32.5元/人，65岁以上（含65岁）中国公民须持身份证或《敬老优待证》；现役军人须持军官证及军人保障卡现役残疾军人须持军残证及军官证；现役士兵须持士兵证；残疾人须持残疾人证；警官须持警官证；军事院校学生须持学员证；学生持中国学生证半票；1.2米以下儿童免票；1.2米以上，1.4米以下儿童半票"

        # 建馆时间  buildingTime
        buildingTime = "公元1087年"

        # 开放时间  openingHours

        openingHours = "开放时间：3月1日——4月底： 8:00——17:30停票，18：15闭馆；5月1日——国庆节 8:00——18：00停票，18：45闭馆；国庆节后——11月底 8:00——17:30停票，18:15闭馆；12月1日——次年2月底 8:00——17:15停票 18:00闭馆"

        # 藏品数量  collectionNum

        collectionNum = "11000余件"

        # 藏品种类  collectionType
        collectionType = "碑林、石刻艺术和其它文物"

        # 展区数量  number
        number = "12个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse117(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(117))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "旺季（3~11月）：08:00~18:00；淡季（12~2月）：08:00~17:30"

        # 藏品数量  collectionNum

        collectionNum = "3万多件"

        # 藏品种类  collectionType
        collectionType = "石器3000件，陶器1.4万件，其他质地器物3700多件，人骨标本200多具，古生物化石和古人类化石标本约200多件"

        # 展区数量  number
        number = "5个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse118(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(118))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "1、每个开放日上午9：00至下午17:30。2、每周二（国家法定节假日除外）及除夕全天闭馆，其余时间开放。"

        # 藏品数量  collectionNum

        collectionNum = "13万件"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse119(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(119))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费不免票,每天向社会最高限量发放免费参观券3000张，每日14时前限2000张，下午16时前限1000张，发完为止，发票时间为每个开放日的9：00—16：30。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "每周二至周日9:00—17:00"

        # 藏品数量  collectionNum

        collectionNum = "600余件(组)"

        # 藏品种类  collectionType
        collectionType = "宝鸡地区考古发现的青铜器、玉器、陶器、金器等精品"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse120(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(120))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        museumName = "西安大唐西市博物馆"

        # 博物馆地点  museumPosition
        museumPosition = "西安西市东北角十字街街心遗址之上"

        # 博物馆类别  buildingType
        i = 0
        buildingType = "兼职博物馆"

        # 门票  ticket
        ticket = "NULL"

        # 建馆时间  buildingTime
        i = 0
        buildingTime = "2010年4月10日"

        # 开放时间  openingHours

        openingHours = "NULL"

        # 藏品数量  collectionNum

        collectionNum = "两万余件"

        # 藏品种类  collectionType
        collectionType = "以西市遗址出土文物和博物馆创办人20多年来收藏的文物为主"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)

        picture = "NULL"

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)

        yield item

    def parse121(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(121))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "每周二至周日9:00—17:00（16:00停止入馆）"

        # 藏品数量  collectionNum

        collectionNum = "约35万余件"

        # 藏品种类  collectionType
        collectionType = "文物涵括从白垩纪的古生物化石标本到旧石器、新石器时代的彩陶文化；从商周以来的青铜器、陶瓷玉器到汉唐的丝绸之路文明；宋、元、明、清的瓷器、木雕、丝织品、绘画。"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse122(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(122))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费（当日凭有效证件领票，每天限时限量免费参观，17:00停止发票，团体参观需提前一天预约）。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开馆时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + " ,星期一闭馆"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "31909余件"

        # 藏品种类  collectionType
        collectionType = "藏有石器、陶器、瓷器、铜器、铁器、书画古籍、杂项、民俗文物、现代书画和古钱币等"

        # 展区数量  number
        number = "9个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse123(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(123))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "兰州市城关区南滨河东路522号"

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "成立时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "09:00-16:00 (1月1日-12月31日 周二-周日)"

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse124(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(124))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "近2万件"

        # 藏品种类  collectionType
        collectionType = "国家一级文物123件，二级文物2008件，三级文物3816件，国宝级文物3件。"

        # 展区数量  number
        number = "4个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse125(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(125))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地理位置":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "免费，但不免票，观众从售票处领取参观券，每日限制参观人数，闭馆半小时前停止发票"

        # 建馆时间  buildingTime
        buildingTime = "1959年9月"

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + " ,星期一闭馆"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "近4万件"

        # 藏品种类  collectionType
        collectionType = "国家一级文物159件，三级以上珍贵文物4000余件"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse126(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(126))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费参观"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + ",每周一闭馆休整"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "馆藏文物14932件/套，其中珍贵文物2193件/套"

        # 藏品种类  collectionType
        collectionType = "以新时期彩陶和民族宗教类文物最具特色，涉及宗教、民俗、政治、经济、军事、生产生活等多个领域"

        # 展区数量  number
        number = "10个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse127(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(127))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费(每天限量2000人入馆)"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "3.2万件(号),其中一级品288件"

        # 藏品种类  collectionType
        collectionType = "有丝毛棉麻织物 (包括锦、绮、绫、罗、纱、缦、绢、印染、刺绣等大量汉唐丝织品，毯、毡、绦带、刺绣等古代毛织品)，多种文字 (汉文、回鹘文、 佉卢文、吐火罗文、梵文、古和田文、吐蕃文、阿拉伯文、粟特文等) 书写的文书、简牍，晋唐时期木雕、泥塑俑像及纸本、绢本人物，花鸟绘画，具有斯基泰文化特征的青铜器，以及新疆各兄弟民族的服饰与工艺品。此外，还有部分古生物化石和古尸标本等。"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse128(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(128))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + " ,星期一闭馆"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "20637件"

        # 藏品种类  collectionType
        collectionType = "藏品类别有石器、陶器、泥塑、木器、铜器、铁器、金银器、文书、木雕、泥俑、绘画、古尸、粮食、干果及各类食品、泥塑、纺织品、干尸等35种。"

        # 展区数量  number
        number = "9个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse129(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(129))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse130(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        # print(names)
        # print(nvalues)

        # 博物馆编号  museumId
        i = list(str(130))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "票\xa0\xa0\xa0\xa0价":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开馆时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    # “九·一八”历史博物馆
    def parse27(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(27))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n','')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地理位置":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        buildingType="Null"
        # i = 0
        # while i < len(names):
        #     if names[i] == "景点级别":
        #         buildingType = nvalues[i].replace('\n', '')
        #         break
        #     i += 1

        # 门票  ticket
        #ticket = "每日发放免费参观券3000张（含预约观众500人），发完为止。"
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        buildingTime="1997年9月"
        # i = 0
        # while i < len(names):
        #     if names[i] == "竣工时间":
        #         buildingTime = nvalues[i].replace('\n', '')
        #         break
        #     i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "；文献、档案资料近100件；大小型场景19组；雕塑4尊；油画、国画等20余幅"

        # 展区数量  number
        number = "7个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "Null"

        # 评分  grade
        grade = "Null"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    #旅顺博物馆
    def parse28(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(28))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        buildingType=""
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket=""
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1


        # 建馆时间  buildingTime
        buildingTime=""
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            buildingTime = "Null"

        # 开放时间  openingHours
        openingHours=""
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = ""
        i = 0
        while i < len(names):
            if names[i] == "数目藏品":
                collectionNum = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品种类  collectionType
        collectionType = "考古、铜器、陶瓷、甲骨、玉器、漆器、珐琅器、书画、碑志、佛教造像、竹木牙雕、新疆文物、外国文物、货币等20个门类"


        # 展区数量  number
        number = "Null"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "Null"

        # 评分  grade
        grade = "Null"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    #沈阳故宫博物院
    def parse29(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(29))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        buildingType = "Null"
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "票价每人60元。"
        # i = 0
        # while i < len(names):
        #     if names[i] == "门票价格":
        #         ticket = nvalues[i].replace('\n', '')
        #         break
        #     i += 1

        # 建馆时间  buildingTime
        buildingTime = "Null"
        # if "竣工时间" in names:
        #     i = 0
        #     while i < len(names):
        #         if names[i] == "竣工时间":
        #             buildingTime = nvalues[i].replace('\n', '')
        #             break
        #         i += 1
        # else:
        #     buildingTime = "Null"

        # 开放时间  openingHours
        openingHours = "4月10日—10月10日，8:30—17:30，16:45停止售票。10月11日—4月09日，9:00—16：30，15:45停止售票。"
        # i = 0
        # while i < len(names):
        #     if names[i] == "开放时间":
        #         openingHours = nvalues[i].replace('\n', '')
        #         break
        #     i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"
        i = 0
        while i < len(names):
            if names[i] == "数目藏品":
                collectionNum = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品种类  collectionType
        collectionType = "Null"

        # 展区数量  number
        number = "Null"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "Null"

        # 评分  grade
        grade = "Null"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    #吉林省自然博物馆
    def parse30(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(30))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        museumName="吉林省自然博物馆"

        # 博物馆地点  museumPosition
        museumPosition="中国吉林省长春市东北师范大学净月校区"

        # 博物馆类别  buildingType
        buildingType = "自然历史类博物馆"

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        buildingTime = "2006年9月10日"

        # 开放时间  openingHours
        openingHours = "常年对外开放，冬季周一休息"

        # 藏品数量  collectionNum
        collectionNum = "收藏3万多号5万1千多件"

        # 藏品种类  collectionType
        collectionType = "Null"

        # 展区数量  number
        number = "Null"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "东北师范大学暨吉林省自然博物馆将以办成全国一流的博物馆为目标，以一流的设施，一流的陈列，一流的服务迎接海内外广大观众。"


        # 评分  grade
        grade = "10"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    #吉林省博物院
    def parse31(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(31))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "吉林省博物院"

            # 博物馆地点  museumPosition
            museumPosition = "吉林省长春市高新技术产业开发区永顺路1666号"

            # 博物馆类别  buildingType
            buildingType = "历史与艺术博物馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1951年12月"

            # 开放时间  openingHours
            openingHours = "9：00—16：30（周一闭馆）"

            # 藏品数量  collectionNum
            collectionNum = "吉林省博物院有文物藏品12万余件，其中一级文物295件、二级文物3379件、三级文物14280件、其它文物近10万件。"


            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "四区"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    #伪满皇宫博物院
    def parse32(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(32))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "伪满皇宫博物院"

            # 博物馆地点  museumPosition
            museumPosition = "吉林省长春市光复北路5号"

            # 博物馆类别  buildingType
            buildingType = "宫廷遗址型博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "1962年12月24日"

            # 开放时间  openingHours
            openingHours = "5月1日至10月7日，展馆开放时间为8:30至17:20；10月1日至翌年4月30日，展馆开放时间为8:30至16:50"


            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "大型基本陈列2个，专题展览3个，举办临时展览33个，中国国内巡展17个，出国展览11个。"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    #东北烈士纪念馆
    def parse33(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(33))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "东北烈士纪念馆"

            # 博物馆地点  museumPosition
            museumPosition = "黑龙江省哈南岗区一曼街241号"

            # 博物馆类别  buildingType
            buildingType = "中国革命纪念馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1948年10月10日"

            # 开放时间  openingHours
            openingHours = "9:00～16:30（周一闭馆）"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "东北烈士纪念馆有相对完善的学术研究机构,研究人员一直从事抗日战争、解放时期地方史研究。"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 铁人王进喜纪念馆
    def parse34(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(34))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "铁人王进喜纪念馆"

            # 博物馆地点  museumPosition
            museumPosition = "黑龙江省大庆市"

            # 博物馆类别  buildingType
            buildingType = "国家AAAA级旅游景点"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1989年"

            # 开放时间  openingHours
            openingHours = "早8:30—晚16:00"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "铁人王进喜纪念馆是大庆人的“西柏坡”，是大庆耀眼的一张名片。"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 爱辉历史陈列馆
    def parse35(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(35))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "瑷珲历史陈列馆"

            # 博物馆地点  museumPosition
            museumPosition = "黑龙江省黑河市爱辉区"

            # 博物馆类别  buildingType
            buildingType = "专题性遗址博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "1975年9月"

            # 开放时间  openingHours
            openingHours = "9:30 - 15:30（周一闭馆）"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "当参观者看完展览来到半景画馆外，沿阶梯向上攀登到展馆顶部，就能俯视波涛滚滚的十里长江，眺望江东64屯，遥看魁星阁和见证松。夏天，可以欣赏展馆四周绿树成荫、鸟语花香和幽雅环境；冬天，可领略到那千里冰封、万里雪飘的北国风光……"


            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 黑龙江省博物馆
    def parse36(self, response):
                # SelectorList
                global buildingTime
                values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
                names = []
                nvalues = []
                for value in values:
                    # Selector
                    name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                    names.extend(name)
                    nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                    nvalues.extend(nvalue)
                print(names)
                print(nvalues)

                # 博物馆编号  museumId
                i = list(str(36))
                while len(i) < 3:
                    i.insert(0, '0')
                museumId = "".join(i)

                # 博物馆名称  museumName
                museumName = "黑龙江省博物馆"

                # 博物馆地点  museumPosition
                museumPosition = "黑龙江省哈尔滨市南岗区"

                # 博物馆类别  buildingType
                buildingType = "综合性博物馆"

                # 门票  ticket
                ticket = "Null"

                # 建馆时间  buildingTime
                buildingTime = "1906年"

                # 开放时间  openingHours
                openingHours = "每周周二至周日"

                # 藏品数量  collectionNum
                collectionNum = "108584件"

                # 藏品种类  collectionType
                collectionType = "历史文物、自然标本、艺术品"

                # 展区数量  number
                number = "Null"

                # 图片  picture
                pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
                picture = pics[0]

                # 用户视频或音频  VideoAudio
                VideoAudio = "Null"

                # 评价  evaluate
                evaluate = "黑龙江省博物馆是国家科普教育基地、省级旅游定点单位、市区级德育教育基地。"


                # 评分  grade
                grade = "10"

                # tableone = {"museumId":museumId,"museumName":museumName}
                # yield tableone
                item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                             museumPosition=museumPosition, buildingType=buildingType,
                                             ticket=ticket, buildingTime=buildingTime,
                                             openingHours=openingHours, collectionNum=collectionNum,
                                             collectionType=collectionType, number=number,
                                             picture=picture, VideoAudio=VideoAudio,
                                             evaluate=evaluate, grade=grade)
                yield item

    # 大庆博物馆
    def parse37(self, response):
                    # SelectorList
                    global buildingTime
                    values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
                    names = []
                    nvalues = []
                    for value in values:
                        # Selector
                        name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                        names.extend(name)
                        nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                        nvalues.extend(nvalue)
                    print(names)
                    print(nvalues)

                    # 博物馆编号  museumId
                    i = list(str(37))
                    while len(i) < 3:
                        i.insert(0, '0')
                    museumId = "".join(i)

                    # 博物馆名称  museumName
                    museumName = "大庆博物馆"

                    # 博物馆地点  museumPosition
                    museumPosition = "黑龙江省大庆市萨尔图区"

                    # 博物馆类别  buildingType
                    buildingType = "综合性国家一级博物馆"

                    # 门票  ticket
                    ticket = "Null"

                    # 建馆时间  buildingTime
                    buildingTime = "2011年11月22日"

                    # 开放时间  openingHours
                    openingHours = "每周二闭馆，其它时间正常开馆，每天开馆时间：9:00，闭馆时间：16:30，中午不休息，节假日正常开馆"


                    # 藏品数量  collectionNum
                    collectionNum = "Null"

                    # 藏品种类  collectionType
                    collectionType = "Null"

                    # 展区数量  number
                    number = "3"

                    # 图片  picture
                    pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
                    picture = pics[0]

                    # 用户视频或音频  VideoAudio
                    VideoAudio = "Null"

                    # 评价  evaluate
                    evaluate = "第三批国家一级博物馆"

                    # 评分  grade
                    grade = "10"

                    # tableone = {"museumId":museumId,"museumName":museumName}
                    # yield tableone
                    item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                                 museumPosition=museumPosition, buildingType=buildingType,
                                                 ticket=ticket, buildingTime=buildingTime,
                                                 openingHours=openingHours, collectionNum=collectionNum,
                                                 collectionType=collectionType, number=number,
                                                 picture=picture, VideoAudio=VideoAudio,
                                                 evaluate=evaluate, grade=grade)
                    yield item

    # 上海博物馆
    def parse38(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(38))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "上海博物馆"

            # 博物馆地点  museumPosition
            museumPosition = "黄浦区人民大道201号"

            # 博物馆类别  buildingType
            buildingType = "综合性博物馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1996年"

            # 开放时间  openingHours
            openingHours = "9:00-17:00"

            # 藏品数量  collectionNum
            collectionNum = "400余件"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "11"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 上海鲁迅纪念馆
    def parse39(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(39))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "上海鲁迅纪念馆"

            # 博物馆地点  museumPosition
            museumPosition = "鲁迅故居"

            # 博物馆类别  buildingType
            buildingType = "人物性纪念馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1951年1月"

            # 开放时间  openingHours
            openingHours = "Null"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "鲁迅纪念馆的陈列，设计理念先进，活化了文物资料，再现了鲁迅精神，受到专家和广大观众的好评。"


            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 中国共产党第一次全国代表大会会址纪念馆
    def parse40(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(40))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "中国共产党第一次全国代表大会会址纪念馆"

            # 博物馆地点  museumPosition
            museumPosition = "上海市兴业路76号"

            # 博物馆类别  buildingType
            buildingType = "全国重点文物保护单位"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1952年"

            # 开放时间  openingHours
            openingHours = "9:00 — 17:00 （周一闭馆）"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "2"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "全国中小学生研学实践教育基地。"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 上海科技馆
    def parse41(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(41))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "上海科技馆"

            # 博物馆地点  museumPosition
            museumPosition = "上海浦东"

            # 博物馆类别  buildingType
            buildingType = "AAAAA级"

            # 门票  ticket
            ticket = "45元/成人"

            # 建馆时间  buildingTime
            buildingTime = "2001年12月18日"

            # 开放时间  openingHours
            openingHours = "9:00～17:15"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "11"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "全国中小学生研学实践教育基地"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 陈云纪念馆
    def parse42(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(42))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "陈云纪念馆"

            # 博物馆地点  museumPosition
            museumPosition = "上海市青浦区练塘镇"

            # 博物馆类别  buildingType
            buildingType = "Null"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "2000年6月6日"

            # 开放时间  openingHours
            openingHours = "Null"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            # pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            # picture = pics[0]
            picture=""

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "故居与民宅融为一体，体现了江南水乡小镇独具韵味的特色。 "

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 南京博物院
    def parse43(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(43))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "南京博物院"

            # 博物馆地点  museumPosition
            museumPosition = "南京市玄武区中山东路321"

            # 博物馆类别  buildingType
            buildingType = "国家级综合性历史艺术博物馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1948年初"

            # 开放时间  openingHours
            openingHours = "周一9：00－12：00/周二至周日9：00－17：00"

            # 藏品数量  collectionNum
            collectionNum = "432768件（2018年）"

            # 藏品种类  collectionType
            collectionType = "馆藏文物上至旧石器时代，下迄当代；既有全国性的，又有地域性的；既有宫廷传世品，又有考古发掘品，还有一部分来源于社会征集及捐赠，均为历朝历代的珍品佳作和备受国内外学术界瞩目的珍品。青铜、玉石、陶瓷、金银器皿、竹木牙角、漆器、丝织刺绣、书画、印玺、碑刻造像等所有文物品类一应俱有，每一品种又自成历史系列，是数千年中华文明历史发展最为直接的见证。"


            # 展区数量  number
            number = "6"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 侵华日军南京大屠杀遇难同胞纪念馆
    def parse44(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(44))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "侵华日军南京大屠杀遇难同胞纪念馆"

            # 博物馆地点  museumPosition
            museumPosition = "南京市建邺区水西门大街418号"

            # 博物馆类别  buildingType
            buildingType = "灾难遗址专史纪念"

            # 门票  ticket
            ticket = "免费开放"

            # 建馆时间  buildingTime
            buildingTime = "2015年12月1日"

            # 开放时间  openingHours
            openingHours = "08:30-16:30（每周二至周日）"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "4"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "侵华日军南京大屠杀遇难同胞纪念馆馆标造型独特，设计新颖，标志融会了南京城墙和国家公祭鼎两种意象。设计者是南京艺术学院何方副教授。"


            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 南通博物苑
    def parse45(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(45))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "南通博物苑"

            # 博物馆地点  museumPosition
            museumPosition = "南通市"

            # 博物馆类别  buildingType
            buildingType = "综合性博物馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1905年"

            # 开放时间  openingHours
            openingHours = "9:00—17:00；16:30谢客入内（周一闭馆）"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "6"

            # 图片  picture
            # pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            # picture = pics[0]
            picture=""

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "2011年12月，获得中央精神文明建设指导委员会授予的“第三批全国文明单位”荣誉称号。"


            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 苏州博物馆 （苏州市博物馆）
    def parse46(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(46))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "苏州博物馆"

            # 博物馆地点  museumPosition
            museumPosition = "江苏省苏州市"

            # 博物馆类别  buildingType
            buildingType = "综合性历史博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "1960年"

            # 开放时间  openingHours
            openingHours = "周二至周日"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "第五届全国文明单位。"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 扬州博物馆
    def parse47(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(47))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "扬州双博馆"

            # 博物馆地点  museumPosition
            museumPosition = "江苏省扬州市文昌西路468号"

            # 博物馆类别  buildingType
            buildingType = "文化博物馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "2005年10月9日"

            # 开放时间  openingHours
            openingHours = "9:00-17:00（每周二至周日） "

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "8"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "全国爱国主义教育示范基地"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 常州博物馆
    def parse48(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(48))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "常州博物馆"

            # 博物馆地点  museumPosition
            museumPosition = "常州市龙城大道1288号"

            # 博物馆类别  buildingType
            buildingType = "地方综合性博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "1958年10月"

            # 开放时间  openingHours
            openingHours = "新馆 2007年4月28日"

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            #pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            #picture = pics[0]
            picture=""
            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "2018年10月，被评为全国中小学生研学实践教育基地。"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 南京市博物总馆
    def parse49(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(49))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "南京市博物总馆"

            # 博物馆地点  museumPosition
            museumPosition = "南京"

            # 博物馆类别  buildingType
            buildingType = "综合性历史艺术类博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "2014年"

            # 开放时间  openingHours
            openingHours = "Null"

            # 藏品数量  collectionNum
            collectionNum = "馆藏文物10万余件（套），其中一级文物395件（套）。"

            # 藏品种类  collectionType
            collectionType = "馆藏文物10万余件（套），其中一级文物395件（套）。"

            # 展区数量  number
            number = "Null"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 浙江省博物馆
    def parse50(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(50))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "浙江省博物馆"

            # 博物馆地点  museumPosition
            museumPosition = "浙江省杭州市西湖区孤山路25号"

            # 博物馆类别  buildingType
            buildingType = "历史综合性博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "1929年"

            # 开放时间  openingHours
            openingHours = "9:00～17:00"

            # 藏品数量  collectionNum
            collectionNum = "馆藏文物达十万余件"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "10+"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 浙江自然博物馆
    def parse51(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(51))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "浙江自然博物院"

            # 博物馆地点  museumPosition
            museumPosition = "杭州市中心西湖文化广场6号"

            # 博物馆类别  buildingType
            buildingType = "国家一级博物馆"

            # 门票  ticket
            ticket = "免费"

            # 建馆时间  buildingTime
            buildingTime = "1929年"

            # 开放时间  openingHours
            openingHours = "9:30-16:00"

            # 藏品数量  collectionNum
            collectionNum = "15万件"

            # 藏品种类  collectionType
            collectionType = "集动物、植物、化石、岩石、矿物、自然艺术等多个门类之收藏精品。"

            # 展区数量  number
            number = "3"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "第十三届全国博物馆十大陈列展览精品奖"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item

    # 中国丝绸博物馆
    def parse52(self, response):
            # SelectorList
            global buildingTime
            values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
            names = []
            nvalues = []
            for value in values:
                # Selector
                name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
                names.extend(name)
                nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
                nvalues.extend(nvalue)
            print(names)
            print(nvalues)

            # 博物馆编号  museumId
            i = list(str(52))
            while len(i) < 3:
                i.insert(0, '0')
            museumId = "".join(i)

            # 博物馆名称  museumName
            museumName = "中国丝绸博物馆"

            # 博物馆地点  museumPosition
            museumPosition = "西湖区玉皇山路"

            # 博物馆类别  buildingType
            buildingType = "丝绸专业博物馆"

            # 门票  ticket
            ticket = "Null"

            # 建馆时间  buildingTime
            buildingTime = "Null"

            # 开放时间  openingHours
            openingHours = "中国丝绸故事一厅、二厅、天蚕灵机厅、织造坊：周一12:00-17:00（法定假日9:00-17:00），周二至周日9:00-17:00。纺织品修复展示馆：周一12:00-17:00（法定假日9:00-17:00），周二至周日9:00-17:00（其中修复保护工作室，双休日及法定假日不对外展示）。新猷资料馆（双休日及法定假日不对外开放）：周一13:00—17:00；周二至周五9:00-11:30，13:00-17:00各展馆16:45停止进馆参观。 "

            # 藏品数量  collectionNum
            collectionNum = "Null"

            # 藏品种类  collectionType
            collectionType = "Null"

            # 展区数量  number
            number = "11"

            # 图片  picture
            pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
            picture = pics[0]

            # 用户视频或音频  VideoAudio
            VideoAudio = "Null"

            # 评价  evaluate
            evaluate = "Null"

            # 评分  grade
            grade = "10"

            # tableone = {"museumId":museumId,"museumName":museumName}
            # yield tableone
            item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                         museumPosition=museumPosition, buildingType=buildingType,
                                         ticket=ticket, buildingTime=buildingTime,
                                         openingHours=openingHours, collectionNum=collectionNum,
                                         collectionType=collectionType, number=number,
                                         picture=picture, VideoAudio=VideoAudio,
                                         evaluate=evaluate, grade=grade)
            yield item


    def parse53(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(53))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n','')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "每日发放免费参观券3000张（含预约观众500人），发完为止。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "6万余件"

        # 藏品种类  collectionType
        collectionType = "珍贵靑铜器、瓷器、竹刻、玉器、书画、金银器、民俗"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse54(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(54))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门\xa0\xa0\xa0\xa0票":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            buildingTime = "2001年"

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "逾万件"

        # 藏品种类  collectionType
        collectionType = "陶瓷、书画、玉石、印章、钱币、邮票"

        # 展区数量  number
        number = "6个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse55(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(55))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门\xa0\xa0\xa0\xa0票":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "2 万多件"

        # 藏品种类  collectionType
        collectionType = "陶瓷器、青铜器、彩塑、砖雕、漆器、书画"

        # 展区数量  number
        number = "7个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse56(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(56))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "21.8万余件"

        # 藏品种类  collectionType
        collectionType = "铜、陶、瓷、金、 银、玉器、货币、书画、民俗、砖雕石刻、文房四宝、革命文物及社会主义建设时期的文物"

        # 展区数量  number
        number = "7个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = []
        picture.append(pics[0])
        picture.append("https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1741020169,218422683&fm=26&gp=0.jpg")
        picture.append("https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1985683497,1296393644&fm=26&gp=0.jpg")


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse57(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(57))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "10万件（2015年）"

        # 藏品种类  collectionType
        collectionType = "陶瓷、砚台、徽墨、书画、徽州三雕、青铜器、玉器、杂项、古籍图书、徽州文书"

        # 展区数量  number
        number = "6个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse58(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(58))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "近17万余件"

        # 藏品种类  collectionType
        collectionType = "陶器、禽类骨骼、石器、石片、骨器、瓷器、书画"

        # 展区数量  number
        number = "15个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = []
        picture.append(pics[0])
        picture.append("http://img4.imgtn.bdimg.com/it/u=3481347143,2046294831&fm=26&gp=0.jpg")
        picture.append("http://img0.imgtn.bdimg.com/it/u=3881843861,1853310863&fm=26&gp=0.jpg")


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse59(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(59))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别" or names[i] == "博物馆级别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "Null"


        # 建馆时间  buildingTime
        if "竣工时间" in names or "开馆时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间" or names[i] == "开馆时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        if "开放时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "开放时间":
                    openingHours = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            openingHours = "Null"

        # 藏品数量  collectionNum
        collectionNum = "1万多件"

        # 藏品种类  collectionType
        collectionType = "旧址、书籍"

        # 展区数量  number
        number = "Null"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse60(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(60))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "锚具、石刻、陶瓷器、船模、器物"

        # 展区数量  number
        number = "11个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse61(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(61))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "石壁雕、火药爆绘壁画、陶器、编钟"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse62(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(62))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        if "开放时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "开放时间":
                    openingHours = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            openingHours = "周二至周日开放，每周日闭馆。上午8：15到11：45，下午14：15到17：15，夏季：上午8：15到11：45，下午15：00到17：45，实行免费"


        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "书籍、服饰、瓷器、物件"

        # 展区数量  number
        number = "12个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse63(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(63))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "3万余件"

        # 藏品种类  collectionType
        collectionType = "墨宝珍迹、影视资料、书籍、手稿、武器"

        # 展区数量  number
        number = "19个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = []
        picture.append(pics[0])
        picture.append("http://img5.imgtn.bdimg.com/it/u=3265380156,3242196795&fm=26&gp=0.jpg")
        picture.append("http://img1.imgtn.bdimg.com/it/u=4012685395,1072487104&fm=26&gp=0.jpg")


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse64(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(64))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "3.4万余件"

        # 藏品种类  collectionType
        collectionType = "青铜器、金银器、陶瓷器、玉石、字画、生物标本"

        # 展区数量  number
        number = "10个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse65(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(65))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称" or names[i] == "中文名":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        # i = 0
        # while i < len(names):
        #     if names[i] == "地\xa0\xa0\xa0\xa0点":
        #         museumPosition = nvalues[i].replace('\n', '')
        #         break
        #     i += 1
        museumPosition = "江西省瑞金市区的象湖镇"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别" or names[i] == "博物馆级别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            buildingTime = "1958年"


        # 开放时间  openingHours
        # i = 0
        # while i < len(names):
        #     if names[i] == "开放时间":
        #         openingHours = nvalues[i].replace('\n', '')
        #         break
        #     i += 1
        openingHours = "8:30 ----- 17:30（夏季）8:30 ----- 17:00（冬季）（旧址景区全年开放，博物馆星期一闭馆检修，法定节假日除外）"

        # 藏品数量  collectionNum
        collectionNum = "10265件"

        # 藏品种类  collectionType
        collectionType = "遗址、图书、杂志、器件、勋章"

        # 展区数量  number
        number = "Null"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse66(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(66))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "972件"

        # 藏品种类  collectionType
        collectionType = "锚具、石刻、陶瓷器、船模、器物"

        # 展区数量  number
        number = "2层"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse67(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(67))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "5000余件"

        # 藏品种类  collectionType
        collectionType = "书籍、文物展品、股票凭证"

        # 展区数量  number
        number = "12个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse68(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(68))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "16万件"

        # 藏品种类  collectionType
        collectionType = "书法、绘画、陶瓷器、铜器、玉器、钱币、玺印、甲骨、竹木牙角器等三十余个门类"

        # 展区数量  number
        number = "5个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = []
        picture.append(pics[0])
        picture.append("https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2028142003,2858521155&fm=26&gp=0.jpg")
        picture.append("https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=4126852762,1479389854&fm=26&gp=0.jpg")


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse69(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(69))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "铁锚、鱼雷、委任状、望远镜、指南针、怀表"

        # 展区数量  number
        number = "8个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse70(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(70))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "四万余件"

        # 藏品种类  collectionType
        collectionType = "简史陈列、陶瓷器、玉器、青铜器、书画、古货币、碑碣、石刻、革命文物等"

        # 展区数量  number
        number = "10个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse71(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(71))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "陶瓷器、青铜器、甲骨文、陶文、封泥、玺印、简牍、汉画像石、书画、善本书等"

        # 展区数量  number
        number = "15个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse72(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(72))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "5万余件"

        # 藏品种类  collectionType
        collectionType = "陶瓷器、玉石器、青铜器、铁器、书画、丝织品和杂项"

        # 展区数量  number
        number = "6个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse73(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(73))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "近8万件"

        # 藏品种类  collectionType
        collectionType = "化石、陶器、瓷器、青铜、玉石、钱币、古角牙木、书画、碑拓、古籍、碑刻、造像、织绣、玺印符牌、民俗服饰及饰品、近现代革命文物等33类"

        # 展区数量  number
        number = "大于4个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse74(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(74))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "13万余件"

        # 藏品种类  collectionType
        collectionType = "史前文物、商周青铜器、历代陶瓷器、玉器等"

        # 展区数量  number
        number = "4个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = []
        picture.append(pics[0])
        picture.append("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=928690041,2112392362&fm=26&gp=0.jpg")
        picture.append("https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1281572346,933772798&fm=26&gp=0.jpg")

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse75(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(75))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "现场免费领取参观券，讲解收费为50元/场"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "Null"

        # 藏品种类  collectionType
        collectionType = "编钟、青铜礼器、酒器、玉器、占卜甲骨、骨蚌器、日用陶器、旧石器时代、新石器时代文物等"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        # pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        # picture = pics[0]
        picture = "https://bkimg.cdn.bcebos.com/pic/b21c8701a18b87d610f548390f0828381f30fd65?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg"


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse76(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(76))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点" or names[i] == "地理位置":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别" or names[i] == "博物馆级别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门\xa0\xa0\xa0\xa0票" or names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            buildingTime = "1958年"


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "40多万余件"

        # 藏品种类  collectionType
        collectionType = "化石、彩陶器、青铜礼器、彩绘陶器及百戏俑、彩绘乐舞俑、唐三彩等"

        # 展区数量  number
        number = "8个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse77(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(77))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "2000余件"

        # 藏品种类  collectionType
        collectionType = "生产劳动画像、建筑类画像、历史故事类、社会生活类画像、天文与神话类等"

        # 展区数量  number
        number = "12个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse78(self, response):
        # SelectorList
        global buildingTime
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(78))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        if "门\xa0\xa0\xa0\xa0票" in names:
            i = 0
            while i < len(names):
                if names[i] == "门\xa0\xa0\xa0\xa0票":
                    ticket = nvalues[i].replace('\n', '')
                    break
                i += 1
        else:
            ticket = "免费"


        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1


        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "80000件"

        # 藏品种类  collectionType
        collectionType = "玉器、书画、青铜、陶瓷等"

        # 展区数量  number
        number = "4个"

        # 图片  picture
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]


        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse105(self, response):
        # SelectorList

        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(105))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "票\xa0\xa0\xa0\xa0价":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "2000多件"

        # 藏品种类  collectionType
        collectionType = "革命文物及历史资料"

        # 展区数量  number
        number = "11个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item
        yield scrapy.Request("https://baike.baidu.com/item/%E4%BA%91%E5%8D%97%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86",
                             callback=self.parse106)

    def parse106(self, response):
        # SelectorList
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(106))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0址":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        if "竣工时间" in names:
            i = 0
            while i < len(names):
                if names[i] == "竣工时间":
                    buildingTime = nvalues[i].replace('\n', '')
                    break
                i += 1

        # 开放时间  openingHours
        openingHours = "NULL"
        # 藏品数量  collectionNum
        collectionNum = "20余万件"

        # 藏品种类  collectionType
        collectionType = "青铜器、古钱币、陶瓷器、古书画、碑贴、邮票及各类工艺品"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]
        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item
        yield scrapy.Request(
            "https://baike.baidu.com/item/%E4%BA%91%E5%8D%97%E6%B0%91%E6%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86",
            callback=self.parse107)

    def parse107(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(107))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "昆明市滇池路1503号"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "票价为每人10元，对未成年人、中小学生、离休干部、现役军人、残疾人、劳模凭证免票。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "正常开放时间为每周二至周日上午9时至下午5时（周一休息）"

        # 藏品数量  collectionNum
        collectionNum = "12万件"

        # 藏品种类  collectionType
        collectionType = "民族古籍、文化遗产、民族服饰、民间美术、民族乐器、传统生产生活技术等"

        # 展区数量  number
        number = "16个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse108(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(108))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "9：00——17：00（周一闭馆）"

        # 藏品数量  collectionNum
        collectionNum = "馆藏文物约10万多件，资料5万多件"

        # 藏品种类  collectionType
        collectionType = "四川旧石器 500多件，巴蜀文物1000余件，汉画像石、画像砖100多件，历代名窑陶瓷器4000多件，宋元以来名家书画5000多件"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse109(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(109))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门\xa0\xa0\xa0\xa0票":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = "全年开放" + " " + nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "超过10万件"

        # 藏品种类  collectionType
        collectionType = "一级文物227件、二级文物284件、三级文物2749件"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse110(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(110))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "旧馆位于重庆市枇杷山正街74号，新馆位于重庆市北碚区金华路398号"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        collectionNum = "11万余件"

        # 藏品种类  collectionType
        collectionType = "涵盖动物、植物、古生物、古人类、旧石器、地质矿产、岩石、土壤等八大学科"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse111(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(111))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "拉萨市罗布林卡东南角"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "夏季：10:00～17:30 冬季：10:00～16:30（周一不能参观）"

        # 藏品数量  collectionNum
        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "各种类型的史前文化遗物、多种质地和造型的佛、菩萨人物造像，历代蘸金粉、银粉、珊瑚粉等手写的藏文典籍，历代中央政府颁给大活佛的金印，金瓶掣签仪式使用的金瓶和玉签，五彩纷呈的唐卡画，各种乐器、法器，具有鲜明的民族特色的手工艺品，别有风格的陶器等等"

        # 展区数量  number
        number = "9个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse112(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(112))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省西安市雁塔区小寨东路91号"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费，凭有效证件换票参观"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        openingHours = "周二至周日全天开放"

        # 藏品数量  collectionNum
        i = 0
        while i < len(names):
            if names[i] == "馆藏文物数量":
                collectionNum = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品种类  collectionType
        collectionType = "馆藏文物上起远古人类初始阶段使用的简单石器，下至1840年前社会生活中的各类器物，时间跨度长达一百多万年"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse113(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(113))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省西安市临潼区秦陵镇"

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "120元人民币/人次，学生证享半价优惠 ；65岁以上老人、残疾人、中国现役军人（含武警）、军队院校学员、退伍老红军战士、革命伤残军人、由家长携带的16岁以下未成年人免费。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum
        i = 0
        while i < len(names):
            if names[i] == "藏品数量":
                collectionNum = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品种类  collectionType
        collectionType = "陶俑、陶马、青铜兵器、铜车马"

        # 展区数量  number
        number = "4个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse114(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(114))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省延安市宝塔区王家坪路"

        # 博物馆类别  buildingType
        buildingType = "革命纪念博物馆"

        # 门票  ticket
        ticket = "免费，需携带身份证。"

        # 建馆时间  buildingTime
        buildingTime = "1950年7月"

        # 开放时间  openingHours
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "文物有3.5万多件，历史照片5500多张，图书资料1.2万余册"

        # 藏品种类  collectionType
        collectionType = "一、二级文物有1700余件，延安时期出版发行的报刊杂志100余种。"

        # 展区数量  number
        number = "6个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse115(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(115))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "陕西省西安市北郊的渭河之畔"

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "旺季70.00元 淡季55.00元"

        # 建馆时间  buildingTime
        buildingTime = "1999年9月30日"

        # 开放时间  openingHours

        openingHours = "3－11月 8：30－19：00， 1月、2月和12月8：30－18：00"

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "3个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse116(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(116))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "西安市文昌门内三学街15号"

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "淡季（12月1日——次年2月底）全票50元/人，半票25元/人，旺季（3月1日——11月底）65元/人，半票32.5元/人，65岁以上（含65岁）中国公民须持身份证或《敬老优待证》；现役军人须持军官证及军人保障卡现役残疾军人须持军残证及军官证；现役士兵须持士兵证；残疾人须持残疾人证；警官须持警官证；军事院校学生须持学员证；学生持中国学生证半票；1.2米以下儿童免票；1.2米以上，1.4米以下儿童半票"

        # 建馆时间  buildingTime
        buildingTime = "公元1087年"

        # 开放时间  openingHours

        openingHours = "开放时间：3月1日——4月底： 8:00——17:30停票，18：15闭馆；5月1日——国庆节 8:00——18：00停票，18：45闭馆；国庆节后——11月底 8:00——17:30停票，18:15闭馆；12月1日——次年2月底 8:00——17:15停票 18:00闭馆"

        # 藏品数量  collectionNum

        collectionNum = "11000余件"

        # 藏品种类  collectionType
        collectionType = "碑林、石刻艺术和其它文物"

        # 展区数量  number
        number = "12个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse117(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(117))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "旺季（3~11月）：08:00~18:00；淡季（12~2月）：08:00~17:30"

        # 藏品数量  collectionNum

        collectionNum = "3万多件"

        # 藏品种类  collectionType
        collectionType = "石器3000件，陶器1.4万件，其他质地器物3700多件，人骨标本200多具，古生物化石和古人类化石标本约200多件"

        # 展区数量  number
        number = "5个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse118(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(118))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "1、每个开放日上午9：00至下午17:30。2、每周二（国家法定节假日除外）及除夕全天闭馆，其余时间开放。"

        # 藏品数量  collectionNum

        collectionNum = "13万件"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse119(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(119))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费不免票,每天向社会最高限量发放免费参观券3000张，每日14时前限2000张，下午16时前限1000张，发完为止，发票时间为每个开放日的9：00—16：30。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "每周二至周日9:00—17:00"

        # 藏品数量  collectionNum

        collectionNum = "600余件(组)"

        # 藏品种类  collectionType
        collectionType = "宝鸡地区考古发现的青铜器、玉器、陶器、金器等精品"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse120(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(120))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0址":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "NULL"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "成立时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "NULL"

        # 藏品数量  collectionNum

        collectionNum = "两万余件"

        # 藏品种类  collectionType
        collectionType = "以西市遗址出土文物和博物馆创办人20多年来收藏的文物为主"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse121(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(121))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "每周二至周日9:00—17:00（16:00停止入馆）"

        # 藏品数量  collectionNum

        collectionNum = "约35万余件"

        # 藏品种类  collectionType
        collectionType = "文物涵括从白垩纪的古生物化石标本到旧石器、新石器时代的彩陶文化；从商周以来的青铜器、陶瓷玉器到汉唐的丝绸之路文明；宋、元、明、清的瓷器、木雕、丝织品、绘画。"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse122(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(122))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费（当日凭有效证件领票，每天限时限量免费参观，17:00停止发票，团体参观需提前一天预约）。"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开馆时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + " ,星期一闭馆"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "31909余件"

        # 藏品种类  collectionType
        collectionType = "藏有石器、陶器、瓷器、铜器、铁器、书画古籍、杂项、民俗文物、现代书画和古钱币等"

        # 展区数量  number
        number = "9个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse123(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(123))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        museumPosition = "兰州市城关区南滨河东路522号"

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "成立时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        openingHours = "09:00-16:00 (1月1日-12月31日 周二-周日)"

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse124(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(124))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "近2万件"

        # 藏品种类  collectionType
        collectionType = "国家一级文物123件，二级文物2008件，三级文物3816件，国宝级文物3件。"

        # 展区数量  number
        number = "4个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse125(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(125))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地理位置":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        buildingType = "NULL"

        # 门票  ticket
        ticket = "免费，但不免票，观众从售票处领取参观券，每日限制参观人数，闭馆半小时前停止发票"

        # 建馆时间  buildingTime
        buildingTime = "1959年9月"

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + " ,星期一闭馆"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "近4万件"

        # 藏品种类  collectionType
        collectionType = "国家一级文物159件，三级以上珍贵文物4000余件"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse126(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(126))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0址":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费参观"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + ",每周一闭馆休整"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "馆藏文物14932件/套，其中珍贵文物2193件/套"

        # 藏品种类  collectionType
        collectionType = "以新时期彩陶和民族宗教类文物最具特色，涉及宗教、民俗、政治、经济、军事、生产生活等多个领域"

        # 展区数量  number
        number = "10个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse127(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(127))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费(每天限量2000人入馆)"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "3.2万件(号),其中一级品288件"

        # 藏品种类  collectionType
        collectionType = "有丝毛棉麻织物 (包括锦、绮、绫、罗、纱、缦、绢、印染、刺绣等大量汉唐丝织品，毯、毡、绦带、刺绣等古代毛织品)，多种文字 (汉文、回鹘文、 佉卢文、吐火罗文、梵文、古和田文、吐蕃文、阿拉伯文、粟特文等) 书写的文书、简牍，晋唐时期木雕、泥塑俑像及纸本、绢本人物，花鸟绘画，具有斯基泰文化特征的青铜器，以及新疆各兄弟民族的服饰与工艺品。此外，还有部分古生物化石和古尸标本等。"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse128(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(128))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        ticket = "免费"

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '') + " ,星期一闭馆"
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "20637件"

        # 藏品种类  collectionType
        collectionType = "藏品类别有石器、陶器、泥塑、木器、铜器、铁器、金银器、文书、木雕、泥俑、绘画、古尸、粮食、干果及各类食品、泥塑、纺织品、干尸等35种。"

        # 展区数量  number
        number = "9个"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse129(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(129))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "门票价格":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "竣工时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item

    def parse130(self, response):
        # SelectorList
        # global buildingTime, openingHours, museumPosition, buildingType, museumName
        values = response.xpath("//div[@class='basic-info cmn-clearfix']/dl")
        names = []
        nvalues = []
        for value in values:
            # Selector
            name = value.xpath(".//dt[@class='basicInfo-item name']//text()").getall()
            names.extend(name)
            nvalue = value.xpath(".//dd[@class='basicInfo-item value']//text()").getall()
            nvalues.extend(nvalue)
        print(names)
        print(nvalues)

        # 博物馆编号  museumId
        i = list(str(130))
        while len(i) < 3:
            i.insert(0, '0')
        museumId = "".join(i)

        # 博物馆名称  museumName
        i = 0
        while i < len(names):
            if names[i] == "中文名称":
                museumName = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆地点  museumPosition
        i = 0
        while i < len(names):
            if names[i] == "地\xa0\xa0\xa0\xa0点":
                museumPosition = nvalues[i].replace('\n', '')
                break
            i += 1

        # 博物馆类别  buildingType
        i = 0
        while i < len(names):
            if names[i] == "类\xa0\xa0\xa0\xa0别":
                buildingType = nvalues[i].replace('\n', '')
                break
            i += 1

        # 门票  ticket
        i = 0
        while i < len(names):
            if names[i] == "票\xa0\xa0\xa0\xa0价":
                ticket = nvalues[i].replace('\n', '')
                break
            i += 1

        # 建馆时间  buildingTime
        i = 0
        while i < len(names):
            if names[i] == "开馆时间":
                buildingTime = nvalues[i].replace('\n', '')
                break
            i += 1

        # 开放时间  openingHours

        i = 0
        while i < len(names):
            if names[i] == "开放时间":
                openingHours = nvalues[i].replace('\n', '')
                break
            i += 1

        # 藏品数量  collectionNum

        collectionNum = "NULL"

        # 藏品种类  collectionType
        collectionType = "NULL"

        # 展区数量  number
        number = "NULL"

        # 图片  picture
        # ch = re.compile(r'<img src="(.*?)"', re.S)
        # pics = response.xpath("//div[@class='summary-pic']/img")
        # print("pics=  ",pics)
        # for pic in pics:
        #     print(pic)
        # # picture = re.findall(ch, pics)[0]
        # # print("pics=  ", picture)
        pics = response.xpath('//div[@class="summary-pic"]//img/@src').extract()
        picture = pics[0]

        # 用户视频或音频  VideoAudio
        VideoAudio = "Null"

        # 评价  evaluate
        evaluate = "环境优美，馆藏丰富。"

        # 评分  grade
        grade = "5分"

        # tableone = {"museumId":museumId,"museumName":museumName}
        # yield tableone
        item = MuseuminformationItem(museumId=museumId, museumName=museumName,
                                     museumPosition=museumPosition, buildingType=buildingType,
                                     ticket=ticket, buildingTime=buildingTime,
                                     openingHours=openingHours, collectionNum=collectionNum,
                                     collectionType=collectionType, number=number,
                                     picture=picture, VideoAudio=VideoAudio,
                                     evaluate=evaluate, grade=grade)
        yield item



