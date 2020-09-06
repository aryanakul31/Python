import xlwt
import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook('IT2017-21.xls')

wb=copy(rb)
w_sheet = wb.get_sheet(0)

w_sheet.write(0,0,"A")
wb.save('IT2017-21.xls')
