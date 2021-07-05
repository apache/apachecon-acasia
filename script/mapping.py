# 将ApacheConAsia讲师信息收集表.xlsx和drawing1.xml文件放到项目根目录
# 将会在根目录生成mapping.csv文件

from xml.dom.minidom import parse
from pypinyin import lazy_pinyin
import xml.dom.minidom
import csv
import openpyxl
 
 # 首先定义一个CSV文件
head =["row","pic","zh_name","en_name","mail","session"]
with open("./mapping.csv","a+",encoding="utf-8",newline="") as f:
   csvf=csv.writer(f)
   csvf.writerow(head)

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("./drawing1.xml")

#打开execl文件
wb=openpyxl.load_workbook("./ApacheConAsia讲师信息收集表.xlsx")

collection = DOMTree.documentElement

# 在集合中获取数据
twoCellAnchors = collection.getElementsByTagName("xdr"+":"+"twoCellAnchor")

# 获取row和pic
for twoCellAnchor in twoCellAnchors:
 
   from1 = twoCellAnchor.getElementsByTagName('xdr'+':'+'from')[0]
   row1=from1.getElementsByTagName('xdr'+':'+'row')[0]
   row=int(row1.childNodes[0].data)

   pic = twoCellAnchor.getElementsByTagName('xdr'+':'+'pic')[0]
   blipFill = pic.getElementsByTagName('xdr'+':'+'blipFill')[0]
   blip = blipFill.getElementsByTagName('a'+':'+'blip')[0]
   if blip.hasAttribute("r"+":"+"embed"):
      pic="picture"+(blip.getAttribute("r"+":"+"embed"))[3:]

   # 获取活跃的表对象
   sheet=wb.active
   # 获取讲师名和邮箱
   zh_name=sheet.cell(row,3).value
   mail=sheet.cell(row,10).value

   # 判断是否为中文名字
   if '\u4e00' <=zh_name <='\u9fff':
      # 将中文姓名转化成英文名
      name_list=lazy_pinyin(zh_name)
      xin=name_list[0]
      ming_list=name_list[1:]
      ming=""
      for i in ming_list:
         ming=ming+i
      en_name=ming.capitalize()+" "+xin.capitalize()
   else:
      en_name=zh_name

   # 关联session表，格式：讲师姓名 <邮箱>
   session=en_name+"<"+mail+">"

   # 将数据写入CSV文件
   data=[
      (row,pic,zh_name,en_name,mail,session)
   ]
   with open("./mapping.csv","a+",encoding="utf-8",newline="") as f:
      csvf=csv.writer(f)
      csvf.writerows(data)
   