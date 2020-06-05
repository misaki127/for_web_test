
#coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def capture(driver,filephoto):  #截取屏幕
	driver.execute_script("""
		  (function () {
		  var y = 0;
		  var step = 100;
		  window.scroll(0, 0);
		  function f() {
		  if (y < document.body.scrollHeight) {
		  y += step;
		  window.scroll(0, y);
		  setTimeout(f, 50);
		  } else {
		  window.scroll(0, 0);
		  document.title += "scroll-done";
		  }
		  }
		  setTimeout(f, 1000);
		  })();
		 """)
	for i in range(30):
		if "scroll-done" in driver.title:
			break
		time.sleep(1)
	beg = time.time()
	for i in range(10):
		driver.save_screenshot(filephoto)
	end = time.time()
	print("截屏操作时间：")
	print(end - beg)


import sys
sys.path.append(r"D:\python\selenium_UI\hydra-digital-village\数字党建")
from SZXC_login import login_web
driver = login_web()
# #url = "http://ceshicun.jgwcjm.com/#/user/login"
# url = 'http://system.nine.kf315.net/#/user/login' #测试环境
# driver = webdriver.Chrome("E:/2345Downloads/chromedriver_win32/chromedriver.exe")  # 创建Chrome浏览器驱动实例
# driver.implicitly_wait(15)  # 设置隐式等待时间
# driver.maximize_window()  # 全屏窗口
# driver.get(url)
# # 登陆
# driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
# driver.find_element_by_xpath("//*[@id='account']").send_keys('13000000098')
# driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('123456q') #测试环境
# #driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('jgw1478')
# driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[3]/div/div/span/button").click()
# driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/span").click()
# driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[1]")
# driver.find_element_by_xpath("//*[@id='root']/div/div/button").click()
# driver.switch_to.default_content()
#组织建设
#测试
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[7]").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[7]/div[2]/a[1]").click()
#线上
# driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[13]").click()
# driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[13]/div[2]/a[1]").click()
#添加
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[1]/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div[1]/i").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div[@class='el-select-dropdown']/div/div[1]/ul/li[1]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/input").send_keys("王测测")
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[3]/div/div/input").send_keys("书记")
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/input").send_keys("处理村内一切事务")
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[5]/div/div/input").send_keys("18770295955")
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[6]/div/div/div[1]/i").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[6]/div/div/div[@class='el-select-dropdown']/div/div[1]/ul/li[1]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
#编辑
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[7]/div/div/a[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/input").send_keys("1")
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
#搜索
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/span/span/input").send_keys("1")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/span/span/span/button").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
driver.refresh()
#删除
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[7]/div/div/a[2]").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")

time.sleep(5)
driver.quit()