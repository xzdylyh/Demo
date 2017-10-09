#_*_coding:utf-8_*_
from Scripts import excel
from Scripts import httpRequest
from Scripts import log
import os
from Scripts import gl
from Scripts import reportLog
import sys



class cRequest(object):

    def __init__(self,url,method,Data):
        self.method = method
        self.url = url
        self.Data = Data

    def send(self):
        try:
            request = httpRequest.httpWebRequest(self.url,self.Data)
            if str(self.method).lower()=='post':
                reponse = request.post()
            if str(self.method).lower()=='get':
                reponse =request.get()
        except Exception,ex:
            return ex.message

        return reponse

#执行调用
class cRun(object):

    def __init__(self):
        #pass
        self.__reportXml = reportLog.cREPORTXML()


    def removeDebugLog(self):
        logPath= gl.logsPath+'debug.log'
        if os.path.exists(logPath):
            os.remove(logPath)


    #获取测试用例绝对路径
    def getTestCasePath(self):
        casePath =gl.dataPath+'TestCase.xlsx'
        log.out().info('获取测试用例路径:'+casePath)
        return casePath

    #获取测试数据
    def getTestData(self):
        testData = []
        try:
            xlsInstance =excel.Excel(self.getTestCasePath())
            flagArr =xlsInstance.getData('flag')
            for i in range(0,len(flagArr)):
                if str(flagArr[i]).lower()=='y':
                    url = xlsInstance.getData('Url')[i]
                    method = xlsInstance.getData('Method')[i]
                    header = xlsInstance.getFormDataDict('Data')[i]
                    testData.append(url)
                    testData.append(method)
                    testData.append(header)
                    tmpVal = 'true'
                    #testData.append('RowEnd')
            #如果tmpVal不等于true说明,表中没有可执行的用例,执行状态都不是y
            if tmpVal <>'true':
                testData[0]='false'
            log.out().info(testData)
        except Exception,ex:
            log.out().debug(ex.message)
            return ex.message
        return testData

    #执行用例中,Y测试条目
    def go(self):

        #self.removeDebugLog() #每次执行清除debug日志
        dataArr = self.getTestData()
        if dataArr[0]<>'false':
            #步长为3,否则越界
            reponse = []
            overStatus = 'PASSED'
            for j in range(0,len(dataArr),3):
                request =cRequest(dataArr[j],dataArr[j+1],dataArr[j+2])
                reponseText = request.send()
                reponse.append(reponseText)
                #print reponse #此处添加结果校验


                if reponseText['code']=='200':
                    resultStatus = 'PASSED'
                else:
                    resultStatus = 'FAILED'
                    overStatus = 'FAILED'
                self.__reportXml.writeReport(gl.curTime,resultStatus,reponseText['code'],reponseText.__str__())

            return reponse

        return '数据表没有可执行用例,请检查状态!'

if __name__=="__main__":
    cRun().go()