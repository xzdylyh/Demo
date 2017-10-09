#*_*coding:utf-8*_*
from selenium import webdriver
from appium import webdriver

#appium webdriver 继承自selenium的webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android' #平台名Android
desired_caps['platformVersion'] = '4.2.2' #这个是模拟器，设置的版本
desired_caps['deviceName'] = 'AndroidEM' #模拟器设置的设备名称
desired_caps['appPackage'] = 'com.android.calculator2' #计算器相对应的包名称
desired_caps['appActivity'] = '.Calculator' #计算器javapackage
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #地址不变

driver.find_element_by_name('1').click()
driver.find_element_by_name('3').click()
driver.find_element_by_name('7').click()
driver.find_element_by_name('+').click()
driver.find_element_by_name('8').click()
driver.find_element_by_name('6').click()
driver.find_element_by_name('5').click()
driver.find_element_by_name('=').click()

driver.quit()
