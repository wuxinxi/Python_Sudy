
from Include.py.init import Student

from Include.py.init2 import Score

import  types


student = Student('wuxinxi', 'Java1305', '安徽亳州')
student.print_info()

print(student.name)

print(type(student))


def fun():
    pass

print(type(fun)==types.FunctionType)

print(dir(student))


sco=Score()
sco.setScore(100)

print(sco.getScore())

sco.score=80
print(sco.score)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')


# python _、__和__xx__的区别

# _,表示私有的属性
# ——,表示避免子类覆盖




