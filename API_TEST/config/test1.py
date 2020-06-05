import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
import time
import pymysql
import pymysql.cursors
import json
import sys
sys.path.append('D:\\python\\API_test\API_excel')
sys.path.append('D:\\python\\API_test\common')
from made_excel import read_excel,write_excel
from request import get_token,api_request,get_cookie
import json
import time

def bug(a):
    if a == (1 or 2):
        print(1)
    elif a == 3 or 4:
        print(3)
    else:
        print(5)

bug(2)


# url = "http://192.168.2.215:10098/hydra-digital-village/api/v1/village-information/add"
#
# json0 = {
#     "address": "浙江省杭州市江干区天城路1号杭州东站",
#     "area": 1500,
#     "ext": [
#         {'address': "[['119.698762','30.352562'],['119.65207','30.17583'],['119.853944','30.174643']]",
#          'name': "测试自然村001", 'naturalVillageNumber': "1302020003214",
#          'villageExtId': "37e7b0b9198d4dc8b049be5d787cff93"}
#     ],
#     "image": "",
#     "introduction": "代码提交的",
#     "latitude": 0,
#     "longitude": 0,
#     "multiple": 0,
#     "perCapitaIncome": 0,
#     "regionCode": "110101",
#     "townshipName": "jgw",
#     "villageId": "1101010021",
#     "villageName": "接口村"
# }
# json1 = json.dumps(json0)
#
# headers = {"Content-Type": 'application/json;charset=UTF-8', 'Cookie': ''}
#
#
# def get_cookie():
#     option = webdriver.ChromeOptions()
#     option.add_argument("headless")
#     driver = webdriver.Chrome(chrome_options=option,
#                               executable_path='E:/2345Downloads/chromedriver_win32 (2)/chromedriver.exe')
#     # driver = webdriver.Chrome('E:/2345Downloads/chromedriver_win32 (2)/chromedriver.exe')
#     driver.implicitly_wait(15)  # 设置隐式等待时间
#     driver.maximize_window()
#     driver.get('http://system.nine.kf315.net/')
#     driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
#     driver.find_element_by_xpath('//*[@id="account"]').send_keys('13000000098')
#     driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/div/div/span/span/input').send_keys('123456q')
#     driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[3]/div/div/span/button').click()
#     driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div').click()
#     time.sleep(2)
#     driver.find_element_by_xpath(
#         "//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[4]").click()
#     driver.find_element_by_xpath('//*[@id="root"]/div/div/button').click()
#     success = 1
#     while success == 1:
#         try:
#             time.sleep(1)
#             assert driver.find_element_by_xpath(
#                 "//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/a[1]/div").text != '组织管理'
#         except:
#             success = 0
#     cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
#     cookiestr = ';'.join(item for item in cookie)
#     driver.quit()
#     return cookiestr
#
#
# cookie = get_cookie()
# headers["Cookie"] = cookie
# r = requests.post(url, data=json1, headers=headers)
# print(r.json())
#
# connection = pymysql.connect(host='192.168.2.214', user='jgw', password='Jgw*31500-2018.6', db='hydra_digital_village',
#                              charset='utf8mb4', port=3306, cursorclass=pymysql.cursors.DictCursor)
#
# cursor = connection.cursor()
#
# household_number = ['1101010021']
#
# # select_sql = "SELECT * FROM hydra_digital_village.t_family_information where household_number = %s AND organization_id = '8137ceb00d5e40f3ac210589fa993eb6'" % household_number
# select_sql = "SELECT * FROM hydra_digital_village.t_village_information where village_number = '1101010021' AND organization_id = '8137ceb00d5e40f3ac210589fa993eb6'"
# select_sql2 = "select * from hydra_digital_village.t_village_information_ext where village_id = (SELECT village_id FROM hydra_digital_village.t_village_information where village_number = '1101010021' AND organization_id = '8137ceb00d5e40f3ac210589fa993eb6')"
# cursor.execute(select_sql)
# all_data1 = cursor.fetchall()
# cursor.execute(select_sql2)
# all_data2 = cursor.fetchall()
# print(all_data1, all_data2)
#
# for hh_num in household_number:
#     select_sql = "SELECT * FROM hydra_digital_village.t_village_information where village_number = '1101010021' AND organization_id = '8137ceb00d5e40f3ac210589fa993eb6'"
#     cursor.execute(select_sql)
#     all_data = cursor.fetchall()
#     print(all_data)
#
# cursor.close()

'''url = 'http://192.168.2.215:10098/hydra-digital-village/api/v1/village-information/list'
headers = {"Content-Type":'application/x-www-form-urlencoded;charset=UTF-8','Cookie':''}
json1 = {'current':'1','flag':'1','pageSize':'10','super-token':'36cd439ab44e48ae81870591e9e24645'}

def get_cookie():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option,executable_path='E:/2345Downloads/chromedriver_win32 (2)/chromedriver.exe')
    #driver = webdriver.Chrome('E:/2345Downloads/chromedriver_win32 (2)/chromedriver.exe')
    driver.implicitly_wait(15)  # 设置隐式等待时间
    driver.maximize_window()
    driver.get('http://system.nine.kf315.net/')
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
    driver.find_element_by_xpath('//*[@id="account"]').send_keys('13000000098')
    driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/div/div/span/span/input').send_keys('123456q')
    driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[3]/div/div/span/button').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div').click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[4]").click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/button').click()
    success = 1
    while success == 1:
        try:
            time.sleep(1)
            assert driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/a[1]/div").text != '组织管理'
        except:
            success = 0
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    driver.quit()
    return cookie

cookie = get_cookie()
#cookie = ['JSESSIONID=B77BFAD394D0B430B21993EFB6D99150', 'loginFrom=http%253A%252F%252Fuser.center.kf315.net%252F%253Fsite%253Dsystem%2526system%253Dhttp%25253A%25252F%25252Fsystem.nine.kf315.net%2526borderColor%253D%252523ffffff%2523%252Fframe%252Fuser%252Flogin', 'aid=96d163bd83d547f99815aac46623db78', 'super-token=d50f213926e64502aeb31df80b61097b']
cookiestr = ';'.join(item for item in cookie)
print(cookie)
headers['Cookie']=cookiestr
r = requests.get(url,data=json1,headers=headers)
print(r.text)
'''
