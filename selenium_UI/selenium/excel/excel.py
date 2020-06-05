import xlrd,xlwt


def read_excel(file):  #读取excel
    excel_list = []
    data = xlrd.open_workbook(file,'r')
    sheetname = data.sheet_names()
    for i in sheetname:
        table = data.sheet_by_name(i)
        rows = table.nrows
        cols = table.ncols
        list2 = []
        for p in rows:
            list1 = []
            for f in cols:
                list1.append(table.cell_value(p,f))
            list2.append(list1)
        excel_list.append(list2)

    return  excel_list,sheetname

def write_excel(filename,sheetname,info_list):#写入一个excel 
    workbook = xlwt.Workbook('utf-8')
    for i in sheetname:
        worksheet = workbook.add_sheet(sheetname)
        for i in range(len(info_list)):
            for a in range(len(info_list[i])):
                worksheet.write(i,a, info_list[i][a])
    workbook.save(filename)







