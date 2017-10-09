
import urllib2
import urllib
import  sys
import cookielib

'''
思路：
1.通过cookie对象下载验证码图片到本地
2.手工填写验证码
3.登录
4.拿到返回的登录信息
'''

#将cookie绑定到对象opener，cookie由cookielib自动管理
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

#验证码url和登录url
codeurl = 'https://secure.elong.com/passport/getValidateCode'
loginurl='https://secure.elong.com/passport/ajax/elongLogin'

#根据验证码地址，下载图片到d:/test.gif
picture = opener.open(codeurl).read()
local = open('d:/test.gif','wb')
local.write(picture)
local.close()

#打开本验证码图片，填写验证码
codePic = raw_input('input please:')

#登录post fromData数据
postData = {'userName':'13718651998',
            'passwd':'yhleng870120',
            'validateCode':codePic,
            'rememberMe':'true'}

#获取的头信息
headers = {
'Accept': '*/*',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}

data = urllib.urlencode(postData)#将数据转换为key1&value&key2&value
request = urllib2.Request(loginurl,data,headers)#发起登录请求
response = opener.open(request)#根据最开始获取的的cookie对象，获取响应信息
result = response.read()#读取
print result