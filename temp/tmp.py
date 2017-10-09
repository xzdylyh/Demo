#-*-coding=utf-8-*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
file=os.path.join(basedir,'report.html')
print(file)

'''
os.system() #?这个方法是直接调用标准C的system()?函数，仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息。
rs = os.popen() #?该方法不但执行命令还返回执行后的信息对象，是通过一个管道文件将结果返回
#好处在于：将返回的结果赋于一变量，便于程序的处理。
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