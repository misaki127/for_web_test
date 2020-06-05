
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
#民生公示
#测试
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[7]").click()
element = driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[7]/div[2]/a[5]")
#线上
# driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[13]").click()
# element = driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[13]/div[2]/a[5]")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[2]/a[1]").click()
#添加
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[1]/div/a/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[2]/div/div/div/span/div/i").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/table[@class='el-year-table']/tbody/tr[1]/td[2]/a").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[3]/div/div/input").send_keys("低保五保")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[5]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[1]/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[3]").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[5]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[2]/div/input").send_keys("1500")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[5]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div/div").click()
time.sleep(1)
list1 = driver.find_elements_by_tag_name("li")
for i in list1:
    if i.text == "B":
        i.click()
    else:
        pass
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[6]/div/button[2]").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
#查看
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[3]/div/div/a[1]").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[6]/div/button").click()
#编辑
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[3]/div/div/a[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[4]/div/div/label[2]/span[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[5]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[1]/div/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[3]").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[5]/div/div/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div/input").send_keys("1500")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/form/div[6]/div/button[2]").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
#搜索
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/span/span/input").send_keys("低保")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/span/span/span/button").click()
capture(driver,filephoto="D:/" + str(time.time())+".png")
driver.refresh()
#删除
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[3]/div/div/a[3]").click()


time.sleep(5)
driver.quit()