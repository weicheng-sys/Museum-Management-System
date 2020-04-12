#-*- codeing=uft-8 -*-
#@Time: 2020/4/11 19:31
#@Author:陈怡婧
#@File ：21山西博物院.py
#@Software:PyCharm

import bs4  #网页解析，获取数据
from bs4 import BeautifulSoup
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定URL，获取网页数据
import xlwt    #进行excel操作
import sqlite3  #进行SQLITE数据库操作

import xlwt,xlrd  #往excel中追加数据使用
from xlutils.copy import copy


def main():   #爬取数据，解析数据
    baseurl="https://baike.baidu.com/item/%E5%B1%B1%E8%A5%BF%E5%8D%9A%E7%89%A9%E9%99%A2"

    #1.爬取网页
    datalist =getdata(baseurl)
    savepath="博物馆信息表.xls"    #总表名称：博物馆信息

    # 3.保存数据
    savedata(datalist,savepath)



#博物馆基础信息表
#博物馆编号，自动生成

#博物馆名称
name=re.compile(r'<h1>(.*)</h1>')

#博物馆地点
position=re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)#如果不去掉空行会爬取不到信息

#博物馆图片链接
picture=re.compile(r'<img src="(.*?)"/>')

#文物数量
total=re.compile(r'文物总数达到\d*件')

#爬取网页
def getdata(baseurl):

            html=askurl(baseurl) #保存获取到的网页源码

         # 2.逐一解析数据
            soup=BeautifulSoup(html,"html.parser")
            item1=soup.find_all('div',class_="main-content")
            data=[]             #保存单个博物馆的信息
            #添加博物馆编号
            data.append('021')

            for item in item1:
                item=str(item) #方便用正则表达式解析

                Name=re.findall(name,item)
                data.append(Name)

            item=soup.find_all('div',class_="basic-info cmn-clearfix")

            item = str(item)  # 方便用正则表达式解析

            Position=re.findall(position,item)[2]   #提取博物馆位置
            Position=re.sub('\n', "", Position)  # 替换/
            data.append(Position)

            Type = re.findall(position, item)[6] #提取博物馆类别
            Type = re.sub('\n', "", Type)  # 替换/
            data.append(Type)

            data.append("")  #展区数量用空来代替

            # Time=  re.findall(position, item)[4]#提取博物馆建馆时间
            # Time = re.sub('\n', "", Time)  # 替换/
            data.append("")

            item2 = soup.find_all('div', class_="summary-pic") # 返回找到的第一个
            item2 = str(item2)
            print(item2)
            photo = re.findall(picture, item2)  # 只返回一个图片链接即可
            data.append(photo)


            data.append("")  #占据宣传视频或音频

            ticket=re.findall(position,item)[7]  #提取博物馆门票
            ticket = re.sub('\n', " ", ticket)  # 替换/
            data.append(ticket)

            opentime=re.findall(position,item)[5]  #提取博物馆开放时间
            opentime = re.sub('\n', " ", opentime)  # 替换/
            data.append(opentime)
            data.append("")  # 评价
            data.append("")  # 评分

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
    workbook = xlrd.open_workbook('博物馆信息表.xls') #读取旧表中的数据
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    row=worksheet.nrows #获取现有行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    sheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    k=0;
    for data in datalist:
        print("第%d条"%k)
        sheet.write(row,k,data)  #数据
        k+=1;

    new_workbook.save(savepath) #保存



if __name__ == "__main__":  #调用函数，一共爬取26次
        main()
        print("爬取完毕")