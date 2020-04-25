import urllib.request
import urllib
import mysql
import re
from bs4 import BeautifulSoup
from urllib.request import quote

def getHtml(url):
    try:
        headers = {             # 设置请求头
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Upgrade-Insecure-Requests': 1,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive'
        }
        h = urllib.request.Request(url, headers=headers)
        h1 = urllib.request.urlopen(h, timeout=100)
        html = h1.read()
    except urllib.error.URLError as e:
        print('time out')
    return html

# 爬取所有博物馆名
def getMuseums():
    bs = BeautifulSoup(getHtml("https://baike.baidu.com/item/%E5%9B%BD%E5%AE%B6%E4%B8%80%E7%BA%A7%E5%8D%9A%E7%89%A9%E9%A6%86/1372604?fr=aladdin"), "lxml")
    items= []
    museums = []
    museum = bs.table.a.next
    for i in range(1,291):
        items.append(museum.string)
        museum = museum.next.next.next

    for museum in items:
        if museum:
            if "馆" in museum or "院" in museum :
                # print(museum)
                museums.append(museum)

    # print(len(museums))
    return museums

# 将每个博物馆名进行url编码
def encoding_url(museums):
    encoding = []
    for museum in museums:
        encoding.append(quote(museum))
        # print(encoding[len(encoding)-1])
    return encoding

# 返回130博物馆在百度新闻的链接列表
def getBaiduNews():
    encodes = encoding_url(getMuseums())
    list = []
    for encode in encodes:
        list.append('https://www.baidu.com/s?ie=utf-8&cl=2&medium=2&rtt=4&bsst=1&rsv_dl=news_t_sk&tn=news&wd="' + encode + '"&pn=0&cl=3&tn=baidulocal')
    return list

# 返回130博物馆在新浪新闻的链接列表
def getSinaNews():
    encodes = encoding_url(getMuseums())
    list = []
    for encode in encodes:
        list.append('https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=1&bsst=1&rsv_dl=news_t_sk&tn=news&word=%22'+ encode+'%22%2B%22%E6%96%B0%E6%B5%AA%E6%96%B0%E9%97%BB%22&pn=0&rsv_sug3=7&rsv_sug4=514&inputT=2377')
    return list

# 返回130博物馆在搜狐新闻的链接列表
def getSouhuNews():
    encodes = encoding_url(getMuseums())
    list = []
    for encode in encodes:
        list.append('https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%22'+encode+'%22%2B%22%E6%90%9C%E7%8B%90%E7%BD%91%22&pn=0')
    return list

# 返回130博物馆在参考新闻的链接列表
def getCankaoNews():
    encodes = encoding_url(getMuseums())
    list = []
    for encode in encodes:
        list.append('https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=1&bsst=1&rsv_dl=news_t_sk&tn=news&word=%22'+encode+'%22%2B%22%E5%8F%82%E8%80%83%E6%B6%88%E6%81%AF%22&rsv_sug3=11&rsv_sug4=634&rsv_sug2=0&inputT=11140&pn=0')
    return list

def getxhwNews():
    encodes = encoding_url(getMuseums())
    list = []
    for encode in encodes:
        list.append('https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=1&bsst=1&rsv_dl=news_t_sk&tn=news&word=%22'+ encode+'%22+%22%E6%96%B0%E5%8D%8E%E7%BD%91%22&rsv_sug3=11&rsv_sug4=530&rsv_sug1=1&rsv_sug2=0&inputT=9132')
    return list
