# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import unquote
from museums import getMuseums, getMuseumsNews, encoding_url
from museumNews.items import MuseumnewsItem


class BaidunewsSpider(scrapy.Spider):
    name = 'baiduNews'
    source = '百度新闻'
    museum_name = ""
    museum_names = getMuseumsNews(encoding_url(getMuseums()))
    def start_requests(self):  # 由此方法通过下面链接爬取页面
        # 定义爬取的链接
        urls = self.museum_names
        for url in urls:
            for i in range(1, 2):  # 页数
                yield scrapy.Request(url=url, callback=self.parse)
                url = re.sub('pn=\d+', "pn=" + str(i * 10), url)

    def parse(self, response):
        results = response.xpath('//div[@class="result"]/h3/a/@href').extract()
        url = response.url
        # print(url)
        museum_name = re.findall(r'%22(.*?)%22', url)[0]
        museum_name = unquote(museum_name)
        for result in results:
            req = scrapy.Request(url=result, callback=self.parseNewsLink)
            req.meta['item'] = museum_name
            yield req

    def parseNewsLink(self, response):
        museum_name = response.meta['item']
        items = MuseumnewsItem()
        items['source'] = self.source
        items['museum_name'] = museum_name
        items['title'] = response.css('div.article-title h2::text').extract_first()
        content = response.css('span.bjh-p::text').extract()  # response.xpath('//*[@id="article"]/div')
        contentStr = "\n".join(content)
        if contentStr.count(museum_name) >= 5:
            items['content'] = contentStr
            items['date'] = response.css('span.date::text').extract_first()
            items['time'] = response.css('span.time::text').extract_first()
            items['publisher'] = response.css('p.author-name::text').extract_first()
            items['img'] = response.css('div.img-container img::attr(src)').extract()
        else:
            items['content'] = ""
        yield items
