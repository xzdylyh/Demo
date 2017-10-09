#coding=utf-8

#-----------------webScrvice需要引用以下包---------------------------
from suds.client import Client
from suds.transport.https import HttpAuthenticated #webservice需要安全难证
#--------------------------------------------------------------------

#带安全验证请求
class WebService(object):
    def __init__(self,url,name,password):
        self.name = name
        self.password = password
        self.url = url

    #安全验证
    def httpAuthenticated(self):
        try:
            t=HttpAuthenticated(username=self.name,password=self.password)
        except Exception,ex:
            print ex.message
        return t

    #建立WebService连接
    #webService.factory创建实例
    #webService.service调用方法
    def createWebService(self,url,t):
        try:
            webService= Client(url,transport=t)
        except Exception,ex:
            msg = ex.message
            return msg
        return webService

    #创建实例
    def createInstancesof(self,webService,instanceName):
        try:
            instanceObj = webService.factory.create(instanceName)
        except Exception,ex:
            return ex.message
        return instanceObj



t = HttpAuthenticated(username='RFCATUSER',password='q123456') #安全验证所需用户，密码
url = "http://hqxt1.sinopec.com:50000/dir/wsdl?p=sa/65bd52bd76de381daf15736a37d13ab1"
test = Client(url,transport=t)
print test

request=test.factory.create('DT_IPM_SEND_PSBUDGET_REQ')

IPM_MSG_HEAD = test.factory.create('MSG_HEAD')

IPM_MSG_HEAD.SENDTIME = '20170421102908'
IPM_MSG_HEAD.RECIVER = 'ECC'
IPM_MSG_HEAD.SENDER = 'IPM'
IPM_MSG_HEAD.INTERFACE_ID = 'PROJECT_CREATE'
IPM_MSG_HEAD.SPRAS = None
IPM_MSG_HEAD.OPERATOR = None
IPM_MSG_HEAD.SYSTEM_ID = None
IPM_MSG_HEAD.PROXY_ID = None
IPM_MSG_HEAD.GUID = None
IPM_MSG_HEAD.MANDT = None
request.IS_MSG_HEAD = IPM_MSG_HEAD
request.IV_BUKRS = "X060"
request.IV_TESTRUN = "X"
dict ={}
request.IT_PSBUDGET=dict
m=test.service.SI_IPM_SEND_PSBUDGET_REQ_A_OUT(request)
print IPM_MSG_HEAD
print  request


