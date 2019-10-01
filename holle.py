from selenium import webdriver
import time
driver = webdriver.Chrome("c:/sdk/chromedriver.exe")
driver.get("http://192.168.1.173:8081/index.html#/login")
input=driver.find_element_by_xpath("//input[@type='text']")
input.send_keys("admin")
out=driver.find_element_by_xpath("//input[@type='password']")
out.send_keys("jingzhi@")
driver.find_element_by_class_name("el-button").click()
driver.find_element_by_class_name('el-icon-menu').click()
# tom=driver.find_element_by_xpath("//input[class='el-input__inner']")
# tom.send_keys("13661471590")
time.sleep(3)
driver.quit()

