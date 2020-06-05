import xlrd
import io

data = xlrd.open_workbook('D:/一户一码.xlsx')
data.sheet_names()
print(str(data.sheet_names()))

file = "D:/log1.txt"
f = open(file,'a+')

table = data.sheet_by_index(0)
row_num = table.nrows
col_num = table.ncols
for i in range(row_num):
    f.write("row:" + str(table.row_values(i))+datetime'\n')
for i in range(col_num):

    f.write("colum:" + str(table.col_values(i))+'\n')
cel_B3 = table.cell(3,2).value
print(cel_B3)
f.close()

