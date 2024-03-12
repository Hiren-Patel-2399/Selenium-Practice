from xlrd import *

# 1) wp to print all studentname and per

# wb=open_workbook("../Excel/demo.xlsx")
# sh=wb.sheet_by_name("Sheet1")
# rows=sh.nrows
# for i in range(rows):
#     data=sh.row_values(i,0,2)
#     print(data)
#
# ['sname', 'per']
# ['Neel', 69.0]
# ['Hiren', 89.0]
# ['Bharat', 90.0]
# ['Deep', 55.0]
#################################################################

# 2) wp to create a dict comprehension student name and branch pair

# wb=open_workbook("../Excel/demo.xlsx")
# sh=wb.sheet_by_name("Sheet1")
# rows=sh.nrows
# d={sh.row_values(i,0,5)[0]: sh.row_values(i,0,5)[4] for i in range(1,rows)}
# print(d)
#
# {'Neel': 'EEE', 'Hiren': 'CS', 'Bharat': 'EC', 'Deep': 'CIVIL'}
##################################################################################################

# 3) wp to create list comprehension studentname only student per is more than 70

# wb=open_workbook("../Excel/demo.xlsx")
# sh=wb.sheet_by_name("Sheet1")
# rows=sh.nrows
# l=[sh.row_values(i,0,1) for i in range(1,rows) if sh.row_values(i,0,2)[1]>70]
# print(l)

# [['Hiren'], ['Bharat']]
####################################################################################################

# 4) wp to create dict comprehension student name and year only the student who pass out after 2019
# wb=open_workbook("../Excel/demo.xlsx")
# sh=wb.sheet_by_name("Sheet1")
# rows=sh.nrows
# d={sh.row_values(i,0,3)[0]:sh.row_values(i,0,3)[2] for i in range(1,rows) if sh.row_values(i,0,3)[2]>2019}
# print(d)
#
# {'Hiren': 2020.0, 'Bharat': 2023.0, 'Deep': 2021.0}
######################################################################################################

# 5) wp to create dict student name as key and list of percentage , yop and branchs as value
d={}
wb=open_workbook("../Excel/demo.xlsx")
sh=wb.sheet_by_name("Sheet1")
rows=sh.nrows
for i in range(1,rows):
    data=sh.row_values(i)
    d[data[0]] = data[1:5]

print(d)