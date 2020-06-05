
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
#数字党建
#测试
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[10]").click()
driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[10]/div[2]/a[5]").click()
#线上
#driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[15]").click()
#党员学习
#driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[15]/div[2]/a[3]").click()
#添加
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[1]/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div").click()
driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[2]").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/input").send_keys("两会")
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='ueditor_0']"))
driver.find_element_by_xpath("/html/body").send_keys("近日，在对毛南族实现整族脱贫作出的重要指示中，习近平总书记强调：确保高质量完成脱贫攻坚目标任务，奋力夺取脱贫攻坚战全面胜利。犹记得2019年全国两会期间，习近平在参加甘肃代表团审议时强调：“今后两年脱贫攻坚任务仍然艰巨繁重，剩下的都是贫中之贫、困中之困，都是难啃的硬骨头。”一年来，为确保脱贫攻坚任务如期完成，习近平先后赴重庆、江西、内蒙古等省区市考察调研，同贫困群众一起拉家常、算收支、想办法……特别是新冠肺炎疫情发生后，习近平结合实际情况，对打赢脱贫攻坚战再部署、再动员。他深入田间地头看产业发展、走进社区家庭倾听百姓心声，引领人民增强脱贫致富的内生动力，完善“造血”能力，巩固脱贫成果，确保脱贫质量。如今，全面建成小康社会迎来收官之年，全国两会召开在即，央视网《联播+》特梳理习近平去年两会以来的扶贫足迹，讲述这一年间总书记一心为民的扶贫故事。")
driver.switch_to.default_content()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
#查看
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[6]/div/div/a[1]").click()
capture(driver,filephoto="D:/"+str(time.time)+".png")
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/button").click()
#编辑
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[6]/div/div/a[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/input").send_keys("人民网")
driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
capture(driver,filephoto="D:/"+str(time.time)+".png")
#搜索
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/span/span/input").send_keys("两会")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/span/span/span/button").click()
capture(driver,filephoto="D:/"+str(time.time)+".png")
driver.refresh()
#删除
driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[1]/td[6]/div/div/a[3]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]").click()
capture(driver,filephoto="D:/"+str(time.time)+".png")

time.sleep(5)
driver.quit()