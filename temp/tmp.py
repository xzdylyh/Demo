#-*-coding=utf-8-*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
file=os.path.join(basedir,'report.html')
print(file)

'''
os.system() #?���������ֱ�ӵ��ñ�׼C��system()?������������һ�����ն�����ϵͳ��������ܻ�ȡ����ִ�к�ķ�����Ϣ��
rs = os.popen() #?�÷�������ִ���������ִ�к����Ϣ������ͨ��һ���ܵ��ļ����������
#�ô����ڣ������صĽ������һ���������ڳ���Ĵ���
'''


def fc(x):
    return x * 2

list = []
for i in [1,2,3,4,5]:
    list.append(i*2)

print(list)
print(map(str,[1,2,3,4,5]))

strdic = '''{'username':'pyhleng','password':'q123456'}
'''
print eval(strdic)
print(eval(strdic)['password'])


def add(x,y):
    return x * y
print reduce(add,[1,2,3,4,5])


print(map(str.title,['abc','def','ghj']))

def fcq(x):
    return x==4
print filter(fcq,[1,3,4,5,4,6,4])


print(map(lambda y: y*2,[1,2,3,4,5]))


def cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print(sorted([1,2,3,4,5]),cmp)

def foo(**kwargs):

    print(kwargs)
    print(kwargs['username'])
    return kwargs

dict =foo(username='abc',password='1234')
print(dict['username'])