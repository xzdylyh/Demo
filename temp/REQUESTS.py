#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup



r1 = requests.get('https://github.com/login')   # 获得get请求的对象
s1 = BeautifulSoup(r1.text, 'html.parser')      # 使用bs4解析HTML对象
token = s1.find('input', attrs={'name': 'authenticity_token'}).get('value')     # 获取登陆授权码，即csrf_token
utf =  s1.find('input',attrs={'name':'utf8'}).get('value')
get_cookies = r1.cookies.get_dict()     # 获取get请求的cookies，post请求时必须携带
'''
print r1.text
print(s1.text)

print(get_cookies)
'''
print(token)
print(utf)

def login_github():
    """
    通过requests模块模拟浏览器登陆GitHub
    :return:
    """
    # 获取csrf_token
    r1 = requests.get('https://github.com/login')   # 获得get请求的对象
    s1 = BeautifulSoup(r1.text, 'html.parser')      # 使用bs4解析HTML对象
    token = s1.find('input', attrs={'name': 'authenticity_token'}).get('value')     # 获取登陆授权码，即csrf_token
    get_cookies = r1.cookies.get_dict()     # 获取get请求的cookies，post请求时必须携带


    print r1.text

    # 发送post登陆请求
    '''
    post登陆参数
    commit    Sign+in
    utf8    ?
    authenticity_token    E961jQMIyC9NPwL54YPj70gv2hbXWJ…fTUd+e4lT5RAizKbfzQo4eRHsfg==
    login    JackUpDown（用户名）
    password    **********（密码）
    '''
    r2 = requests.post(
        'https://github.com/session',
        data={
            'commit': 'Sign+in',
            'utf8': '?',
            'authenticity_token': token,
            'login': 'JackUpDown',
            'password': '**********'
        },
        cookies=get_cookies     # 携带get请求的cookies
                       )
    login_cookies = r2.cookies.get_dict()   # 获得登陆成功的cookies，携带此cookies就可以访问任意GitHub页面

    # 携带post cookies跳转任意页面
    r3 = requests.get('https://github.com/settings/emails', cookies=login_cookies)
    print(r3.text)