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

#ִ�е���
class cRun(object):

    def __init__(self):
        #pass
        self.__reportXml = reportLog.cREPORTXML()


    def removeDebugLog(self):
        logPath= gl.logsPath+'debug.log'
        if os.path.exists(logPath):
            os.remove(logPath)


    #��ȡ������������·��
    def getTestCasePath(self):
        casePath =gl.dataPath+'TestCase.xlsx'
        log.out().info('��ȡ��������·��:'+casePath)
        return casePath

    #��ȡ��������
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
            #���tmpVal������true˵��,����û�п�ִ�е�����,ִ��״̬������y
            if tmpVal <>'true':
                testData[0]='false'
            log.out().info(testData)
        except Exception,ex:
            log.out().debug(ex.message)
            return ex.message
        return testData

    #ִ��������,Y������Ŀ
    def go(self):

        #self.removeDebugLog() #ÿ��ִ�����debug��־
        dataArr = self.getTestData()
        if dataArr[0]<>'false':
            #����Ϊ3,����Խ��
            reponse = []
            overStatus = 'PASSED'
            for j in range(0,len(dataArr),3):
                request =cRequest(dataArr[j],dataArr[j+1],dataArr[j+2])
                reponseText = request.send()
                reponse.append(reponseText)
                #print reponse #�˴���ӽ��У��


                if reponseText['code']=='200':
                    resultStatus = 'PASSED'
                else:
                    resultStatus = 'FAILED'
                    overStatus = 'FAILED'
                self.__reportXml.writeReport(gl.curTime,resultStatus,reponseText['code'],reponseText.__str__())

            return reponse

        return '���ݱ�û�п�ִ������,����״̬!'

if __name__=="__main__":
    cRun().go()