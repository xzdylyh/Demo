#*_*coding:utf-8*_*

import unittest
from selenium import webdriver
import time,os
from Scripts import BSTestRunner

class Test_apiTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.url = r"http://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_searchBD(self):
        ie = self.driver.get(self.url)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestSuite()
    #suite.addTest(Test_apiTest().test_searchBD())
    unittest.TestLoader().loadTestsFromTestCase(Test_apiTest())
    #unittest.TextTestRunner().run(suite)
    #basedir = os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(r'd:\demo\temp','report.html')
    re_open = open(file,'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open,title='report',description="test ruesult")
    runner.run(suite)