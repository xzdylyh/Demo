#-*-coding=utf-8-*-
try:
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.by import By
except ImportError,ex:
    print(ex.message)

ie = webdriver.Ie()
ie.get('https://test.puhuijia.com/phjpc-web-front/login_8.html')

try:
    ie.find_element_by_link_text('免费注册').click()

    #WebDriverWait(ie,10,1).until(ec.title_is(r'快速注册-普惠家'))
    print ie.title

    ie.find_element_by_id('memberName_regiest').send_keys('xzdylyh')
    ie.find_element_by_id('password_regiest').send_keys('yhleng123')
    ie.find_element_by_id('memberPhone').send_keys('13756818991')
    ie.find_element_by_id('captcha').send_keys('$0')
    ie.find_element_by_id('telcode').send_keys('$0')
    ie.find_element_by_id('commenedId').send_keys('18745105246')
    ie.find_element_by_id('xy').click()

    ie.find_element_by_link_text('注册').click()
except NoSuchElementException,ex:
    print(ex.message)

