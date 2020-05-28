# -*- coding: utf-8 -*-
import scrapy
from museumNews.items import MuseumnewsItem
from museums import getxhwNews
import re
from urllib.parse import unquote

class PachongSpiderSpider(scrapy.Spider):
    name = 'xhw_spider'
    museum_name = ""
    museum_names = getxhwNews()

    def start_requests(self):  # 由此方法通过下面链接爬取页面
        # 定义爬取的链接
        urls = self.museum_names
        for url in urls:
            for i in range(1, 10):  # 页数
                yield scrapy.Request(url=url, callback=self.parse)
                url = re.sub('pn=\d+', "pn=" + str(i * 10), url)

    def parse(self, response):
        results = response.xpath('//div[@class="result"]/h3/a/@href').extract()
        url = response.url
        museum_name = re.findall(r'%22(.*?)%22+', url)[0]
        museum_name = unquote(museum_name)
        for result in results:
            if "http://www.xinhuanet.com/" in result:
                req = scrapy.Request(url=result, callback=self.parse_item)
                req.meta['item'] = museum_name
                yield req


    def parse_item(self, response):
        #print(response.url)
        #print(response.text)
        museum_name = response.meta['item']
        i = MuseumnewsItem()
        content = response.xpath('//*[@id="p-detail"]/p/text()').extract()
        contentStr = " ".join(content)
        if contentStr.count(museum_name) >= 1:
            i["museumName"] = museum_name
            i["source"] = "新华网"
            i["newsTitle"] = response.xpath("/html/head/title/text()").extract_first()
            i["newsContent"] = "\n".join(content)
            if response.xpath('//*[@id="p-detail"]/p/img/@src').extract_first():
                itemimg = re.split("/", response.url)[:-1]
                itemPic = "/".join(itemimg)
                i["newsPicture"] = itemPic+'/'+response.xpath('//*[@id="p-detail"]/p/img/@src').extract_first()
            else:
                i["newsPicture"] = response.xpath('//*[@id="p-detail"]/p/img/@src').extract()
            i["publishTime"] = response.xpath("/html/body/div[2]/div[3]/div/div[2]/span[1]/text()").extract_first()
            i["publisher"] = "新华网"
        else:
            i['newsContent'] = ""
        yield i

