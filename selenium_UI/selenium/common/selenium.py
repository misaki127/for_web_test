import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import io



def getdriver(url):
	driver = webdriver.Chrome("E:/2345Downloads/chromedriver_win32/chromedriver.exe")#创建Chrome浏览器驱动实例
	driver.implicitly_wait(15)#设置隐式等待时间
	driver.maximize_window()#全屏窗口
	driver.get(url)
	return driver

def getelement(driver,mode,address):#确定用户元素定位方式
	if mode == "id":
		element = driver.find_element_by_id(address)
	elif mode == "classname":
		element = driver.find_element_by_class_name(address)
	elif mode == "name":
		element = driver.find_element_by_name(address)
	elif mode == "tagname":
		element = driver.find_element_by_tag_name(address)
	elif mode == 'linktext':
		element = driver.find_element_by_link_text(address)
	elif mode == 'partialtext':
		element = driver.find_element_by_partial_link_text(address)
	elif mode == 'xpath':
		element = driver.find_element_by_xpath(address)
	elif mode == 'css':
		element = driver.find_element_by_css_selector(address)
	else:
		print ("元素定位方式输入错误，请修改后重试！" + str(mode))
	return element

def getevent(driver,event,element,string,xpath):
	if event == "click":
		element.click()
	elif event == "sendkeys":
		element.send_keys(string)
	elif event == "asserttest":
		asserttest(driver,xpath,string)
	elif event == "infarme":
		driver.switch_to.frame(element)
	elif event == 'clear':
		element.clear()
	elif event == 'select':
		select(element).select_by_visible_text(string)
	else:
		print ("操作方式输入错误，请按规范输入！"+ str(event))

def getevents(event,driver,string,i):
	if event == 'quit':
		driver.quit()
	elif event == 'sleep':
		time.sleep(int(string))
	elif event == 'outfarme':
		driver.switch_to.default_content()
	elif event == 'screenshot':
		filephoto = "D:/" + str(i) + ".png"
		capture(driver,filephoto)
	else:
		print("操作方式输入错误，请按规范输入！" + str(event))

def asserttest(driver,xpath,string):
	try:
		assert driver.find_element_by_xpath(xpath).text == string
	except AssertionError:
		print ("error!")


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

def tag_name(driver,event,string):#无论如何都找不到元素时，可以使用此方法
	elements = driver.find_element_by_tag_name(event)
	for i in elements:
		if i.text == string:
			i.click()
			break
	return i