#*_*coding:utf-8*_*

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.by import By
import time

driver = webdriver.Ie()
driver.get('https://www.baidu.com/')
#driver.switch_to.frame('f')
'''
driver.switch_to_alert().accept()
driver.switch_to_window()
driver.switch_to_frame()
driver.switch_to_active_element()
driver.switch_to_default_content()
'''
try:
    '''
    WebDriverWait(driver,timeout,poll_frequency)在单位时间内，检测元素是否存在。返回bool型
    :parameter
    driver 驱动
    timeout等待时间
    poll_frequency检测时间间隔
    -------------------------------------------------------------------
    一般WebDriverWait配合until和until_not使用
    在单位时间内，until直到返回True，until_not相返
    WebDriverWait(driver,timeout,poll_frequency).unitl(ex.presence_of_element_located((By.ID,"kw")))
    需要使用到的包：
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ex
    from selenium.webdriver.common.by import By
    －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    presence_of_element_located是判断元素是否存在
    ex下还有很多的方法供使用，例如，判断复选是否是勾选等
    *****************************************************************
    使用时需要注意事项:ex.presence_of_element_located((By.ID,"kw"))
    这个方法，要有两个括号，因为参数只能是一个元组
    '''
    WebDriverWait(driver,5,0.5).until(ex.presence_of_element_located((By.ID,"kw")))
    #输入selenium 搜索
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()


    #移动到 设置
    element = driver.find_element_by_name('tj_settingicon')
    ActionChains(driver).move_to_element(element).perform()

    #单击，弹出的Ajax
    driver.find_element_by_link_text('搜索设置').click()


    #下拉列表处理
    element = driver.find_element_by_id("nr")
    element.find_element_by_xpath("//option[@value='50']").click()
    time.sleep(2)

    #span元素，关闭 X按钮
    driver.find_element_by_xpath("//span[@class='pfpanelclose close briiconsbg']").click()

    #driver.execute_script("alert('test')")  #execute_script可以执行javascript脚本
    jsStr = "var kw = document.getElementById('kw') ;kw.value='javascript';"
    driver.execute_script(jsStr)

    '''
    #保存设置
    driver.find_element_by_link_text('保存设置').click()
    time.sleep(2)
    driver.switch_to.alert.accept() #Alert消息框处理
    '''
    '''
    #找到输入框  右键  发送a快捷键
    right_element=driver.find_element_by_id('adv_keyword')
    ActionChains(driver).context_click(right_element).perform()
    driver.find_element_by_id('adv_keyword').send_keys('a')
    time.sleep(2)
    #driver.find_element_by_class_name('pfpanelclose close briiconsbg').click()
    '''

except NoSuchElementException,ex:

    print(ex.message)
