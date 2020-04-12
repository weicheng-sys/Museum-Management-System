#-*- coding=utf-8 -*-
#@Time : 2020/4/10 20:23
#@Author : LGT
#@Software: PyCharm

from bs4 import BeautifulSoup   #网页解析
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL获取网页数据
import xlwt     #进行excel操作
import xlrd
from xlutils.copy import copy
import os

def main():
    baseurl = "https://baike.baidu.com/item/%E9%81%B5%E4%B9%89%E4%BC%9A%E8%AE%AE%E7%BA%AA%E5%BF%B5%E9%A6%86"
    # 1.爬取网页
    datalist=getData(baseurl)
    savepath="D:\python\work\demo\软工\博物馆信息.xls"
    saveData(datalist,savepath)
    #askURL("https://baike.baidu.com/item/%E9%81%B5%E4%B9%89%E4%BC%9A%E8%AE%AE%E7%BA%AA%E5%BF%B5%E9%A6%86")

findName=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findType=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findPlace=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findNumber=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)
findTime=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findImgSrc=re.compile(r'<img src="(.*?)"/>',re.S)
findTicket=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)
findOpenTime1=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findOpenTime2=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)
findItemNumber=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)
findItemType=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)

def getData(baseurl):
    data=[]
    html=askURL(baseurl)
    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="basic-info cmn-clearfix"):
        #print(item)


        item=str(item)

        name=re.findall(findName,item)[0]
        #print(name)

        type=re.findall(findType,item)[1]
        #print(type)

        place=re.findall(findPlace,item)[2]
        #print(place)

        time=re.findall(findTime,item)[3]
        #print(time)


        opentime1=re.findall(findOpenTime1,item)[4]
        #print(opentime)

    data.append(name)
    data.append(place)
    data.append(type)

    for item in soup.find_all('div', class_="body-wrapper"):
        item = str(item)
        #print(item)
        number = re.findall(findNumber,item)[1][70:73]
        #print(number)
        data.append(number)

    for item in soup.find_all('div',class_="summary-pic"):
        item=str(item)
        img=re.findall(findImgSrc,item)[0]
        #print(img)
    data.append(time)
    data.append(img)
    data.append(" ")


    for item in soup.find_all('div',class_="main-content"):
        item=str(item)

        ticket=re.findall(findTicket,item)[80]
        #print(ticket)

        opentime2=re.findall(findOpenTime2,item)[78]
        #print(opentime2[5:])
    opentime=opentime2[5:]+opentime1
    data.append(ticket)
    data.append(opentime)
    for item in soup.find_all('div',class_="main-content"):
        item=str(item)
        itemnumber=re.findall(findItemNumber,item)[49][195:201]
        itemtype=re.findall(findItemType,item)[49][201:210]
        #print(itemtype)

        #print(itemnumber)
    data.append(itemnumber)
    data.append(itemtype)
    return data



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



def saveData(datalist,savepath):
    print("save......")

    rb=xlrd.open_workbook(savepath)
    wb=copy(rb)
    sheet=wb.get_sheet(0)
    for j in range(1, 12):
        sheet.write(1, j, datalist[j-1])
    os.remove(savepath)
    wb.save(savepath)





if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()