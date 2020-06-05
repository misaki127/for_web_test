#encoding = utf-8
from selenium import webdriver
import requests
import time
import json
import io




def get_cookie(url,account,password):#获得cookie
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option,executable_path='E:/2345Downloads/chromedriver_win32 (2)/chromedriver.exe')
    #driver = webdriver.Chrome('E:/2345Downloads/chromedriver_win32 (2)/chromedriver.exe')
    driver.implicitly_wait(15)  # 设置隐式等待时间
    driver.maximize_window()
    driver.get(url)
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
    driver.find_element_by_xpath('//*[@id="account"]').send_keys(account)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/div/div/span/span/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div[3]/div/div/span/button').click()
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[@class="ant-select-selection__rendered"]').click()
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
    cookiestr = ';'.join(item for item in cookie)
    driver.quit()
    return cookiestr



def get_token(login_url,login_json,headers,org_url,sys_url):#得到token
    try:
        r = requests.post(login_url,json=login_json,headers=headers)
        r.raise_for_status()
    except:
        print("登陆失败")
    token = json.loads(r.text)['results']['token']
    headers["Cookie"]="super-token="+str(token)
    headers["isAdmin"]="false"
    r = requests.post(org_url, headers=headers, json={})
    r = requests.post(sys_url, headers=headers, json={})
    return headers


def api_request(event,api,url1,json_info,headers):
    url = url1 + api
    if event == 'get':
        try:
            r = requests.get(url,params=json_info,timeout=30,headers=headers)
            r.raise_for_status()
            return r.text
        except:
            print('请求失败')

    elif event == 'post':
        try:
            r = requests.post(url,json=json_info,headers=headers)
            r.raise_for_status()
            return r.text
        except:
            print('请求失败')

    elif event == 'put':
        try:
            r = requests.put(url,data=json_info,headers=headers)
            r.raise_for_status()
            return r.text
        except:
            print('请求失败')

    elif event == 'delete':
        try:
            r = requests.delete(url,headers=headers)
            r.raise_for_status()
            return r.text
        except:
            print('请求失败')

    elif event == 'options':
        try:
            r = requests.options(url,headers=headers)
            r.raise_for_status()
            return r.text
        except:
            print('请求失败')

    else:
        raise SyntaxError
        print('请求类型错误')

