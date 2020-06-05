# D:/python/TEST.PY
# -*- coding:UTF-8 -*-
#基础包：excel的封装

import xlrd

workbook = None

def open_excel(path):
    #打开excel
    #path:打开excel文件的位置
    global workbook
    if (workbook == None):
        workbook = xlrd.open_workbook(path,on_demand=True)

def get_sheet(sheetName):
    #获取页名
    #sheetName:页名  return workbook
    global workbook
    return workbook.sheet_by_name(sheetName)

def get_rows(sheet):
    #获取行号
    return sheet.nrows

def get_content(sheet,row,col):
    #获取表格中的内容，row：行，col：列
    return sheet.cell(row,col).value

def get_cols(sheet):
    #获取列号
    return sheet.ncols

def release(path):
    #释放excel减少内存
    global workbook
    workbook.release_resources()
    del workbook
    #没有验证是否可用

#待新增