# -*- coding: utf-8 -*-
import scrapy
import re
from museumNews.items import MuseumnewsItem
from museums import getCankaoNews
from urllib.parse import unquote

class CankaoNewsSpider(scrapy.Spider):
    name = 'cankaoNews'
    museum_names = getCankaoNews()
    def start_requests(self):
        urls = self.museum_names
        for url in urls:
            for i in range(1, 10):  # 页数
                yield scrapy.Request(url=url, callback=self.parse)
                url = re.sub('pn=\d+', "pn=" + str(i * 10), url)

    def parse(self, response):
        url = response.url
        museum_name = re.findall(r'%22(.*?)%22%2B', url)[0]
        museum_name = unquote(museum_name)
        newsdivs = response.xpath('//*[@id="content_left"]/div[2]/div')       #获取每个单元
        data = []
        for item in newsdivs:
            url = item.xpath(".//h3/a/@href").get()#获取每个单元链接
            data.append(url)
            for url in data:
                if 'http://www.cankaoxiaoxi.com' in url:#进入下一链接
                    # print(scrapy.Request(url, callback=self.parse_item))
                    req = scrapy.Request(url, callback=self.parse_item)
                    req.meta['item'] = museum_name
                    yield req
                else:
                    pass

    def parse_item(self, response):
        museum_name = response.meta['item']
        i = MuseumnewsItem()
        i["museumName"] = museum_name
        i["source"] = "参考消息网"
        content = response.xpath('//*[@id="ctrlfscont"]/p/text()').extract()
        contentStr = " ".join(content)
        if contentStr.count(museum_name) >= 1:
            i["newsTitle"] = response.xpath("/html/head/title/text()").extract()[0]#各级结构
            i['newsContent'] = "".join(content)
            i['newsPicture']=response.xpath('//*[@id="ctrlfscont"]/p[1]/a/img/@src').extract()
            if len(i['newsPicture'])==0:
                i['newsPicture'] = response.xpath('//*[@id="ctrlfscont"]/p[2]/a/img/@src').extract()
            # print(dict(i))
            i["publishTime"] = response.xpath("//*[@id='pubtime_baidu']//text()").getall()[0]
            i["publisher"] = "".join(response.xpath("//*[@id='source_baidu']//text()").extract())
        else:
            i['newsContent']=""
        yield i







