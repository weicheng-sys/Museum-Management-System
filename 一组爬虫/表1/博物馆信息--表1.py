#-*- codeing=uft-8 -*-
#@Time: 2020/4/7 17:38
#@Author:陈怡婧
#@File ：博物馆信息.py
#@Software:PyCharm


import bs4  #网页解析，获取数据
from bs4 import BeautifulSoup
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定URL，获取网页数据
import xlwt    #进行excel操作
import sqlite3  #进行SQLITE数据库操作



def main():
    baseurl="https://baike.baidu.com/item/%E5%9B%BD%E5%AE%B6%E4%B8%80%E7%BA%A7%E5%8D%9A%E7%89%A9%E9%A6%86/1372604?fr=aladdin"

    #1.爬取网页
    datalist =getdata(baseurl)
    savepath="博物馆连接总表.xls"

    # 3.保存数据
    savedata(datalist,savepath)




#博物馆详情链接的规则
findlink=re.compile(r'href="(.*?)"')  #创建正则表达式对象，表示规则，字符串模式


#爬取网页
def getdata(baseurl):
            html=askurl(baseurl) #保存获取到的网页源码

         # 2.逐一解析数据
            soup=BeautifulSoup(html,"html.parser")
            item2=soup.find_all('table')[0] #只爬第一个表格
            print(item2)
            data=[]  #保存一个博物馆的连接
            for item1 in item2:
                for item in item1:
                    item=str(item) #方便用正则表达式解析

                #博物馆的名字，连接
                    link=re.findall(findlink,item)   #re库来通过正则表达式查找指定字符串
                    data.append(link)   #添加链接
                    print(data)
            return data


#得到指定一个URL的网页内容
def askurl(url):
    head={  #模拟浏览器头部信息，给百度服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3314.0Safari / 537.36SE2.XMetaSr1.0"
    }
    #用户代理，表示告诉百度服务器我们是什么类型机器，浏览器
    #本质上是告诉浏览器我们可以接受什么水平的内容

    req=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(req)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#保存数据
def savedata(datalist,savepath):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet("博物馆连接总表",cell_overwrite_ok=True)  # 创建工作表
     #写入数据，第一参数表行，第二个数据表示列
    sheet.write(0,0,"博物馆链接")
    k=1;
    for data in datalist:
        print("第%d条"%k)
        if data!="":
            sheet.write(k,0,data)  #数据
            k+=1;

    book.save(savepath) #保存



if __name__ == "__main__":#调用函数
    main()
    print("爬取完毕")