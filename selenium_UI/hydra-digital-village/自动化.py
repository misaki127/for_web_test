import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import io
import xlrd


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

def getevent(driver,event,element,string):
	if event == "click":
		element.click()
	elif event == "sendkeys":
		element.send_keys(string)
	# elif event == "asserttest":
	# 	asserttest(driver,xpath,string)
	elif event == "infarme":
		driver.switch_to.frame(element)
	elif event == 'clear':
		element.clear()
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

# def set_style(name,height,bold=False):
#     style = xlwt.XFStyle()
#     font = xlwt.Font()
#     font.name = name
#     font.bold = bold
#     font.color_index = 4
#     font.height = height
#     style.font = font
#     return style

def read_excel(file,all_content):
	wb = xlrd.open_workbook(filename=file)
	table = wb.sheet_by_index(0)
	
	for i in range(table.nrows):
		row_content = []
		for j in range(table.ncols):
			ctype = table.cell(i, j).ctype              # 获取单元格返回的数据类型
			cell_value = table.cell(i, j).value         # 获取单元格内容
			if ctype == 2 and cell_value % 1 == 0:      # 是否是数字类型
				cell_value = int(cell_value)
			elif ctype == 3:                            # 是否是日期
				date = datetime(*xldate_as_tuple(cell_value, 0))
				cell_value = date.strftime('%Y/%m/%d %H:%M:%S')
			elif ctype == 4:                            # 是否是布尔类型
				cell_value = True if cell_value == 1 else False
			row_content.append(cell_value)
		all_content.append(row_content)
	return wb

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
	
'''def write_excel(i,endstr,fileexcel):
	new_wb = load_workbook(fileexcel)
	new_ws = active
	str1 = "F" + str(i)
	new_ws[str1] = endstr
	wb.save(fileexcel)'''

def write_file(f,str1):
	f.write("测试结果:")
	f.write(str1)
	f.write('\n')

def tag_name(driver,event,string):#无论如何都找不到元素时，可以使用此方法
	elements = driver.find_element_by_tag_name(event)
	for i in elements:
		if i.text == string:
			i.click()
			break
	return i

all_content = []
fileexcel = str(input('请输入测试用例模板路径，文件为excel文件格式，模板下载链接为：待定'))
file = str(input('请输入日志存放地址：'))
wb = read_excel(fileexcel,all_content)
f=open(file,'a')

endstr = ""

driver = getdriver(all_content[1][2])

errorNum = 0
success = False
while errorNum < 5 and not success:
	try:
		for i in range(2,len(all_content)):
			try:
				string = str(all_content[i][4]) #内容
				address = str(all_content[i][3]) #地址
				mode = str(all_content[i][1]) #定位方式
				event = str(all_content[i][2]) #操作方法
				if event in ["outfarme","sleep","screenshot","quit","screenshot"]:
					getevents(event,driver,string,i)
				else:
					element = getelement(driver,mode,address)
					getevent(driver,event,element,string)

				endstr = "OK"
				
			except:
				
				endstr = "error!"

			#write_excel(i,endstr,fileexcel)
			str1 = str(all_content[i][6]) + ':' + endstr
			write_file(f,str1)

		success = True
	except:
		errorNum += 1
		if errorNum >= 5:
			break

f.close()