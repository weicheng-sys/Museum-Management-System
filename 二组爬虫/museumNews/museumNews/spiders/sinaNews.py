# -*- coding: utf-8 -*-
import scrapy
from museumNews.items import MuseumnewsItem
from museums import getSinaNews
import re
from urllib.parse import unquote

class SinaNews(scrapy.Spider):
    name = 'SinaNews'
    museum_name = ""
    museum_names = getSinaNews()

    def start_requests(self):  # 由此方法通过下面链接爬取页面
        # 定义爬取的链接
        urls = self.museum_names
        for url in urls:
            for i in range(1, 5):  # 页数
                yield scrapy.Request(url=url, callback=self.parse)
                url = re.sub('pn=\d+', "pn=" + str(i * 10), url)

    def parse(self, response):
        results = response.xpath('//div[@class="result"]/h3/a/@href').extract()
        url = response.url
        # print(url)
        museum_name = re.findall(r'%22(.*?)%22%2B', url)[0]
        museum_name = unquote(museum_name)
        for result in results:
            req = scrapy.Request(url=result, callback=self.parse_item)
            req.meta['item'] = museum_name
            yield req

    def parse_item(self, response):
        museum_name = response.meta['item']
        i = MuseumnewsItem()
        i["museumName"] = museum_name
        i["source"] = "新浪新闻"
        content = response.xpath('//div[@id="article"]/div//text()').extract()
        contentStr = " ".join(content)
        if contentStr.count(museum_name) >= 2:
            i["newsTitle"] = response.xpath('//h1[@class="main-title"]/text()').extract()[0]
            i["newsContent"] = " ".join(content).replace("\t", "").replace("\n", " ")
            i["newsPicture"] = response.xpath('//*[@id="0"]/@src').extract()
            datetime = response.xpath('//span[@class="date"]/text()').extract()[0]
            i["publishTime"] = datetime.replace("年", "-").replace("月", "-").replace("日", "")
            i["publisher"] = response.xpath('//div[@class="date-source"]/a/text()').extract()[0]
        else:
            i["newsTitle"] = ""
            i['newsContent'] = ""
        yield i
















