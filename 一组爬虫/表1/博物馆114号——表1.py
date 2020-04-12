#-*- coding=utf-8 -*-
#@Time : 2020/4/12 16:40
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
findPlace=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findOpenTime=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findTicket=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
findItemNumber=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)
findItemType=re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)

def main():
    baseurl = "https://baike.baidu.com/item/%E5%BB%B6%E5%AE%89%E9%9D%A9%E5%91%BD%E7%BA%AA%E5%BF%B5%E9%A6%86"
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
        #print(name)

        place = re.findall(findPlace, item)[1]
        #print(place)

        opentime = re.findall(findOpenTime, item)[2]
        #print(opentime)

        ticket=re.findall(findTicket,item)[4]
        #print(ticket)

    type="革命纪念馆"
    time="1950年7月"
    number=6

    itemnumber="文物有3.5万多件，历史照片5500多张，图书资料1.2万余册"
    itemtype="一、二级文物有1700余件，延安时期出版发行的报刊杂志100余种。"

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
        sheet.write(10, j, datalist[j - 1])
    os.remove(savepath)
    wb.save(savepath)



if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()