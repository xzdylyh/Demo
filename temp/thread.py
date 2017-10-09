#_*_coding:utf-8_*_
try:
    import threading
    import re
except ImportError,ex:
    print('import error:'+ex.message)
'''
def testThread(num):
    num += 4
    print(num)

t1 = threading.Thread(target=testThread,name='thread1',args=(7,))
t1.start()
print(t1.name)
t1.join()
'''
'''
try:
    print('a')
except TypeError,ex:
    print('b')
finally:
    print('c')
'''


#装饰器
def before(fun):
    def tmpFunc():
        print('before print')
        fun()
    return tmpFunc

def after(fun):
    def tmpFunc():
        fun()
        print('after print')
    return tmpFunc


@before
@after
def func():
    print 'this is function'

if __name__=="__main__":
    func()
    a = re.search('e',"abcedf")
    if a is not None:
        print a.group()
    else:
        print(a)
    #搜索和匹配区别
    b = re.match('e','abcdef')
    print(b)
    help(re)
