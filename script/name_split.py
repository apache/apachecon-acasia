# Put the 活动行名单.xlsx file in the project root directory,will be generated in the root directory name_split.csv file

import csv
import openpyxl

 # First, define a CSV file
head =["Email","FirstName","LastName"]
with open("./name_split.csv","a+",encoding="utf-8",newline="") as f:
   csvf=csv.writer(f)
   csvf.writerow(head)


# Open the EXECL file
collect=openpyxl.load_workbook("./活动行名单.xlsx")

# Gets the active table object
collect_active=collect.active

for cell in collect_active['C']:
   if cell.row!=1:
      email=cell.value
      cell_row=cell.row
      name=collect_active.cell(cell_row,2).value

      # Judge whether it is a Chinese name
      if '\u4e00' <= name <='\u9fff':
         name_list=list(name)
         firstName=name_list[0]
         lastName=""
         for i in name_list[1:]:
            lastName=lastName+i
      else:
         firstName=name
         lastName=""

      # Write data to a CSV file
      data=[
         (email,firstName,lastName)
      ]
      with open("./name_split.csv","a+",encoding="utf-8",newline="") as f:
         csvf=csv.writer(f)
         csvf.writerows(data)

   