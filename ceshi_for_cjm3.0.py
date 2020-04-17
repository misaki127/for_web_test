import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import io

class Test():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)#10秒智能等待时间
    self.vars = {}
    
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_(self,file):
    self.driver.get("http://four.system.jgwcjm.com/#/user/login")#打开网页
    # 2 | setWindowSize | 1920x1040 |  | 
    self.driver.set_window_size(1920, 1040)
    # 3 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    '''for i in range(60):            # 循环60次，从0至59
        if i >= 59 :               # 当i大于等于59时，打印提示时间超时
            print("timeout")    
            break
        try:                       # try代码块中出现找不到特定元素的异常会执行except中的代码
            if self.driver.find_element(By.ID, "account").click(): # 如果能查找到特定的元素id就提前退出循环
                break
        except:                    # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
            print("wait for find element")
        time.sleep(1)'''
    self.driver.find_element(By.ID, "account").click()
    # 5 | type | id=account | 13000000098 | 
    self.driver.find_element(By.ID, "account").send_keys("13000000098")
    # 6 | click | css=.ant-input-affix-wrapper > .ant-input |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".ant-input-affix-wrapper > .ant-input").click()
    # 7 | type | css=.ant-input-affix-wrapper > .ant-input | jgw9800 | 
    self.driver.find_element(By.CSS_SELECTOR, ".ant-input-affix-wrapper > .ant-input").send_keys("jgw9800")
    # 8 | click | css=.ant-btn |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()
    # 9 | mouseOver | css=.ant-btn |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".ant-btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | mouseOut | css=.ant-btn |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | click | css=.ant-select-selection-selected-value |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-selection-selected-value").click()
    # 12 | click | css=.ant-select-dropdown-menu-item-active |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
    # 13 | click | css=.ant-btn |  | 
    element1 = self.driver.find_element_by_xpath("/html/body/div/div/div/button")
    self.driver.execute_script("arguments[0].click();", element1)
   
    # 14 | selectFrame | relative=parent |  | 
    self.driver.switch_to.default_content()
    try:
        time.sleep(5)
        #检查展示页面的第一行数据
        assert self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/div/div").text==  "全部角色"
 		#检查展示页面的第二行数据
        assert self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div").text ==  '企业'
        print("验证通过！")
        file.write("验证通过！")
    except AssertionError:
    	print("error!")
    	file.write("验证失败！")
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//div[@id='root']/div/div/div[2]/div[2]/div[4]/span").click()
    print("ok")

file = open("D:/test.txt","a")

for i in range(80):#执行次数
	file.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
	WEB = Test()
	WEB.setup_method()
	WEB.test_(file)
	WEB.teardown_method()
	file.write("\n")
	time.sleep(600)#每次执行之间的间隔时间

file.close()



