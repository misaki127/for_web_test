#enconding:utf-8

from selenium import webdriver

def login_web():
    # url = "http://ceshicun.jgwcjm.com/#/user/login"  #线上
    url = 'http://system.nine.kf315.net/#/user/login'  # 测试环境
    driver = webdriver.Chrome("E:/2345Downloads/chromedriver_win32/chromedriver.exe")  # 创建Chrome浏览器驱动实例
    driver.implicitly_wait(15)  # 设置隐式等待时间
    driver.maximize_window()  # 全屏窗口
    driver.get(url)
    # 登陆
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
    driver.find_element_by_xpath("//*[@id='account']").send_keys('13000000098')
    driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('123456q')  # 测试环境
    # driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('jgw1478') #线上
    driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[3]/div/div/span/button").click()
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/span").click()
    driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[1]")
    driver.find_element_by_xpath("//*[@id='root']/div/div/button").click()
    driver.switch_to.default_content()
    return driver