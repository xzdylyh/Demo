
#coding=utf-8
from suds.client import Client
from suds.transport.https import HttpAuthenticated #webservice需要安全难证

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
dict ={'PRNAM':'BJ0672','GJAHR':'2017','POSID':'','PSPID':'BJ067230','YBUDGET':'600000','TBUDGET':'600000'}

request.IT_PSBUDGET=dict
m=test.service.SI_IPM_SEND_PSBUDGET_REQ_A_OUT(request)

#m=test.service.SI_IPM_SEND_PSBUDGET_REQ_A_OUT(IPM_MSG_HEAD,'x','x060','')
print m
print IPM_MSG_HEAD
print  request


