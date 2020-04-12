#-*- coding=utf-8 -*-
#@Time : 2020/4/11 19:53
#@Author : LGT
#@Software: PyCharm

import xlwt

workbook=xlwt.Workbook(encoding="utf-8",style_compression=0)
worksheet=workbook.add_sheet('博物馆基础信息表',cell_overwrite_ok=True)
col=('博物馆编号','博物馆名称','博物馆地点','博物馆类别','展区数量','建馆时间','图片','用户视频或音频','门票','开放时间','藏品数量','藏品种类','评价','评分')
for i in range(0,14):
    worksheet.write(0, i, col[i])
i=105
for j in range(1,27):
    worksheet.write(j,0,i)
    i=i+1
workbook.save('博物馆信息.xls')

