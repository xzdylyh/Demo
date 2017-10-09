#_*_coding:utf-8*_*
import os
import logging
from logging.handlers import RotatingFileHandler
import gl

def logout():
    #################################################################################################
    #定义一个RotatingFileHandler，最多备份1个日志文件，每个日志文件最大10M
    Rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=1)
    Rthandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(levelno)d] %(levelname)s: %(message)s ')
    Rthandler.setFormatter(formatter)
    logging.getLogger('').addHandler(Rthandler)
    ################################################################################################
logPath = gl.projectPath +"\\logs\\"

class out(object):
    def __init__(self):
        self.basicConfig()


    def basicConfig(self):
        logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(levelno)d] %(levelname)s: %(message)s ',
                                datefmt='%Y.%m.%d %H:%M:%S__',
                                filename='d:\demo\logs\debug.log',
                                filemode='a'
                                )

    def debug(self,message):
        logging.debug(message)
        #QTable.Ui_MainWindow().textBrowserInfo(message)
    def info(self,message):
        logging.info(message)
        #QTable.Ui_MainWindow().textBrowserInfo(message)
    def warning(self,message):
        logging.warning(message)
        #QTable.Ui_MainWindow().textBrowserInfo(message)


if  __name__=="__main__":
   out().debug('1234')

