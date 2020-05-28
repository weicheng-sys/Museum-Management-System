import scrapy
import re
from museumNews.items import MuseumnewsItem
from urllib.parse import unquote
from museums import getSouhuNews

class SouhuSpider(scrapy.Spider):
    name = 'souhuNews'
    source = '搜狐新闻'
    museum_names = getSouhuNews()

    def start_requests(self):  # 由此方法通过下面链接爬取页面
        urls = self.museum_names
        for url in urls:
            for i in range(1, 10):  # 页数
                yield scrapy.Request(url=url, callback=self.parse)
                url = re.sub('pn=\d+', "pn=" + str(i * 10), url)

    def parse(self, response):
        results = response.xpath('//div[@class="result"]/h3/a/@href').extract()
        url = response.url
        # print(url)
        museum_name = re.findall(r'%22(.*?)%22%2B', url)[0]
        museum_name = unquote(museum_name)
        for result in results:
            req = scrapy.Request(url=result, callback=self.parseNewsLink)
            req.meta['item'] = museum_name
            yield req

    def parseNewsLink(self,response):

        museum_name = response.meta['item']

        link_list = response.xpath("//div[@class='article-content-wrapper']").extract()

        for link in link_list:
            item = MuseumnewsItem()

            #博物馆名
            item["museumName"] = museum_name

            #爬取源
            item["source"] = "搜狐新闻"

            content = response.xpath(".//div/p/text()").extract()
            contentStr = " ".join(content)
            if contentStr.count(museum_name) >= 1:
                # 新闻名称
                title = response.xpath(".//h2[@class='title-info']/text()").extract()[0]
                item['newsTitle'] = title.replace(" ", "").replace("\n", "")

                # 新闻内容
                item['newsContent'] = "\n".join(content)

                # 新闻图片
                item['newsPicture'] = response.xpath("//*[@id='articleContent']/div[1]/p[1]/img/@src").extract()

                # 发布时间
                item['publishTime'] = response.xpath(".//footer/span[@class='time']/text()").extract()[0]

                # 发布方
                item['publisher'] = response.xpath(".//span[@class='name']/text()").extract()[0]
            else:
                item['newsContent'] = ""
            yield item


