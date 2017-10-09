#_*_coding:utf-8_*_
import os
import sys
import time
global dataPath #data目录
global rootPath #磁盘根目录
global scriptPath #Scripts目录
global reporterPath #reporter目录
global logsPath #logs目录
global BIIPath #BII目录
global projectPath #项目目录
global curTime #当前日期时间
global stepNumber #步骤编号
global curTimeStr
overStatus = 'PASSED'

#跨文件使用变量
def init():
    global _overallStatusDict
    _overallStatusDict = {}

def setOverallStatus(key,value):
    _overallStatusDict[key]=value

def getOverallStatus(key):
    return _overallStatusDict[key]

curTimeStr = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime()).decode('utf-8')
curTime = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime()).decode('utf-8')
projectPath = os.path.dirname(os.getcwd())+"\\"
rootPath = os.getcwd().split('\\')[0]+'\\'
reporterPath = projectPath+'Reporter\\'
logsPath = projectPath+'logs\\'
dataPath = projectPath+'Data\\'
scriptPath = os.getcwd()+'\\'

dicTo = {}

if __name__=="__main__":
    print curTime
    print projectPath
    print dataPath
    print rootPath
    print scriptPath
    print reporterPath
    print logsPath