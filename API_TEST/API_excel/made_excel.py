#enconding = utf-8

import xlrd
import xlwt




def read_excel(filename,sheet_name): #读取excel表，返回一个包含所有数据列表
    datas = xlrd.open_workbook(filename,'r+')
    sheet_names = datas.sheet_names()

    list2 = []
    if sheet_name in sheet_names:
        table = datas.sheet_by_name(sheet_name)
        num_row = table.nrows
        num_col = table.ncols
        for i in range(num_row):
            list1 = []
            for a in range(num_col):

                list1.append(str(table.cell_value(i,a)))

            list2.append(list1)
        return list2
    else:
        raise NameError

def write_excel(filename,sheetname,info_list):#写入一个excel
    workbook = xlwt.Workbook('utf-8')
    worksheet = workbook.add_sheet(sheetname)
    for i in range(len(info_list)):
        for a in range(len(info_list[i])):
            worksheet.write(i,a, info_list[i][a])
    workbook.save(filename)




