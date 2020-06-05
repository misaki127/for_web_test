#encoding = utf-8

import sys
sys.path.append('D:\\python\\API_test\API_excel')
sys.path.append('D:\\python\\API_test\common')
from made_excel import read_excel,write_excel
from request import get_token,api_request
import json
import time
import pymysql

with open('config.json','r', encoding='UTF-8') as f:    #读取参数文件，获得参数数据
	json_data = json.load(f)


excel_list = read_excel(json_data["excel_info"][0]["excel_file"],json_data["excel_info"][0]["sheetname"])   #读取测试用例excel文件，存入列表中


headers = json_data["headers"][0]        #从参数文件取出headers
login_json = {"account":json_data["SZXC"][0]["account"],"password":json_data["SZXC"][0]["password"]}  #从参数文件取出登陆json

headers = get_token(json_data["SZXC"][0]["login_url"],login_json,headers,json_data["SZXC"][0]["set_org_url"],json_data["SZXC"][0]["set_sys_url"])  #获取token
#链接sql
connect = pymysql.connect(host=json_data["SQL"][0]["host"],user=json_data["SQL"][0]["user"],password=json_data["SQL"][0]["password"],db=json_data["SQL"][0]["database"],charset='utf8mb4',port=3306,cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()



for i in range(1,len(excel_list)):   #执行测试用例，将结果存入列表
	url = excel_list[i][2]
	api = excel_list[i][3]
	request_json = json.loads(excel_list[i][4])
	event = excel_list[i][5]
	r = api_request(event,api,url,request_json,headers)
	excel_list[i][7] = r
	sql = excel_list[i][6]  #执行SQL语句，返回结果，存入列表
	if len(sql) == 0:
		excel_list[i][8] = 'null'
	else:
		cursor.execute(sql)
		sql_data = cursor.fetchall()
		excel_list[i][8] = str(sql_data)

cursor.close()
timedata = time.time()    #用时间戳命名结果报告
filename = "D:/python/API_TEST/report/report" + str(int(timedata)) + ".xlsx"
sheetname = '一村一码报告'
write_excel(filename,sheetname,excel_list)   #写入结果报告
