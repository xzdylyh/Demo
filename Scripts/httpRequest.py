#*_*coding:utf-8*_*
from requests import Request,Session
import json
from Scripts import log
class httpWebRequest(object):
    def __init__(self,url,postData):
        self.url = url
        self.postData =postData
        self.__s = self.session()

    def session(self):
        log.out().info('创建Session对象')
        return Session()


    def post(self):
        try:
            reponse = self.__s.post(self.url,data=self.postData)
            log.out().info(reponse.json())

        except Exception,ex:
            log.out().debug(ex.message)
        return reponse.json()

    def get(self):
        try:
            request = self.__s.get(self.url)
            log.out().info(request.json())
        except Exception,ex:
            log.out().debug(ex.message)
        return request.json()

if __name__=='__main__':
    postdata = '''{'userName':'13718651996',
            'passwd':'yhlxxxx870120',
            'validateCode':'abc',
            'rememberMe':'true'}'''
    url = 'https://secure.elong.com/passport/ajax/elongLogin'
    request = Session().post(url,data=eval(postdata))
    print(request.json())

