#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup



r1 = requests.get('https://github.com/login')   # ���get����Ķ���
s1 = BeautifulSoup(r1.text, 'html.parser')      # ʹ��bs4����HTML����
token = s1.find('input', attrs={'name': 'authenticity_token'}).get('value')     # ��ȡ��½��Ȩ�룬��csrf_token
utf =  s1.find('input',attrs={'name':'utf8'}).get('value')
get_cookies = r1.cookies.get_dict()     # ��ȡget�����cookies��post����ʱ����Я��
'''
print r1.text
print(s1.text)

print(get_cookies)
'''
print(token)
print(utf)

def login_github():
    """
    ͨ��requestsģ��ģ���������½GitHub
    :return:
    """
    # ��ȡcsrf_token
    r1 = requests.get('https://github.com/login')   # ���get����Ķ���
    s1 = BeautifulSoup(r1.text, 'html.parser')      # ʹ��bs4����HTML����
    token = s1.find('input', attrs={'name': 'authenticity_token'}).get('value')     # ��ȡ��½��Ȩ�룬��csrf_token
    get_cookies = r1.cookies.get_dict()     # ��ȡget�����cookies��post����ʱ����Я��


    print r1.text

    # ����post��½����
    '''
    post��½����
    commit    Sign+in
    utf8    ?
    authenticity_token    E961jQMIyC9NPwL54YPj70gv2hbXWJ��fTUd+e4lT5RAizKbfzQo4eRHsfg==
    login    JackUpDown���û�����
    password    **********�����룩
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
        cookies=get_cookies     # Я��get�����cookies
                       )
    login_cookies = r2.cookies.get_dict()   # ��õ�½�ɹ���cookies��Я����cookies�Ϳ��Է�������GitHubҳ��

    # Я��post cookies��ת����ҳ��
    r3 = requests.get('https://github.com/settings/emails', cookies=login_cookies)
    print(r3.text)