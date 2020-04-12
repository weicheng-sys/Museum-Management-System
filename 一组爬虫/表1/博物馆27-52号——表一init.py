#-*- codeing = utf-8 -*-
#@Time : 2020/4/12 18:04
#@Author : 张拓
#@File : museum_index.py
#@Software : PyCharm

#引入正则表达式库
import re

#模拟浏览器发送请求
import urllib.request,urllib.error

#操作excel表
import xlrd
import xlwt

#读取网页内容
from bs4 import BeautifulSoup

datalist =[]    #爬取到的信息

def main():
    spider27()

    print(datalist)

    #excel表的保存位置
    savepath = ".\\博物馆基础信息27-52.xls"
    #3.保存到excel表
    saveData(datalist,savepath)


#1.获取到第i个博物馆url
def getURL(i):

    #整个表
    workbook = xlrd.open_workbook('博物馆链接总表.xls')
    #第一个表
    worksheet = workbook.sheets()[0]

    #去掉前后的字符串，只保留链接
    url=re.sub( r"text:'" ,"",str(worksheet.cell(i-1, 0)))
    url=re.sub( r"'","",url)

    return url



def spider27():
    url = getURL(27)
    datalist.append(getData27(url))

#博物馆名称
findName = re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)
#27博物馆地点
findPosition =re.compile(r'<dd class="basicInfo-item value">(.*?)</dd>',re.S)

# 2.爬取网页并解析
def getData27(url):

    # 每次请求返回的页面内容
    html = askURL(url)

    # 把页面内容转化成bs树形结构
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="basic-info cmn-clearfix"):
        data = []
        item = str(item)
        # print(item)

        try:
            # 博物馆名称
            name = re.findall(findName, item)[0].replace("\n", '')
            # print(name)
            data.append(name)


            # print(data)
        except Exception:
            print("没有找到")
        return data


#2.1模拟浏览器访问网页
def askURL(url):

    #请求头
    header={
        #伪装浏览器
        "User-Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.130Safari / 537.36"
    }
    #根据url和请求头，包装成一次请求
    request = urllib.request.Request(url,headers=header)

    #返回的页面内容
    html=""

    try:
        #进行一次请求的，得到响应
        response = urllib.request.urlopen(request)
        #把响应的页面内容进行解码，方便阅读
        html=response.read().decode("utf-8")
        #print(html)
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


#3.保存到excel表
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    #设置表头
    col = ("博物馆编号", "名称", "地点", "类别", "展区数量")
    for i in range(0, 5):
        worksheet.write(0, i, col[i])

    #设置博物馆编号
    for i in range(1,27):
        worksheet.write(i,0,str(i+26).zfill(3))

    for i in range(0,26):
        print("第%d条" % (i + 27))

        #每个博物馆的数据
        data = datalist[i]
        print(data)
        worksheet.write(i + 1,1,data)  # 数据
        pass
    workbook.save(savepath)
    pass


if __name__ == '__main__':
    main()