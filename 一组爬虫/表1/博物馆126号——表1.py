#-*- coding=utf-8 -*-
#@Time : 2020/4/13 18:23
#@Author : LGT
#@Software: PyCharm

from bs4 import BeautifulSoup   #网页解析
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL获取网页数据
import xlwt     #进行excel操作
import xlrd
from xlutils.copy import copy
import os

findName=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findType=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findPlace=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findTime=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findOpenTime=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)


def main():
    baseurl = "https://baike.baidu.com/item/%E9%9D%92%E6%B5%B7%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1627225"
    # 1.爬取网页
    datalist=getData(baseurl)
    savepath="D:\python\work\demo\软工\博物馆信息.xls"
    saveData(datalist,savepath)



def askURL(url):
    head={          #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
    }                       #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器我们可以接受什么水平的文件内容）
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def getData(baseurl):
    data = []
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="basic-info cmn-clearfix"):
        item=str(item)
        #print(item)

        name = re.findall(findName, item)[0]
        # print(name)

        type = re.findall(findType, item)[1]
        # print(type)

        place = re.findall(findPlace, item)[2]
        # print(place)

        time = re.findall(findTime, item)[3]
        # print(time)

        opentime = re.findall(findOpenTime, item)[4]+"周一闭馆"
        # print(opentime)
    number="10"
    itemnumber="馆藏文物14932件/套，其中珍贵文物2193件/套"
    itemtype="以新时期彩陶和民族宗教类文物最具特色，涉及宗教、民俗、政治、经济、军事、生产生活等多个领域"
    ticket="免费"

    data.append(name)
    data.append(place)
    data.append(type)
    data.append(number)
    data.append(time)
    data.append(" ")
    data.append(" ")
    data.append(ticket)
    data.append(opentime)
    data.append(itemnumber)
    data.append(itemtype)

    return data




def saveData(datalist,savepath):
    print("save......")
    rb = xlrd.open_workbook(savepath)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    for j in range(1, 12):
        sheet.write(22, j, datalist[j - 1])
    os.remove(savepath)
    wb.save(savepath)



if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()