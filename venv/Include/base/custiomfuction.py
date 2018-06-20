def myAbs(n):
    if n > 0:
        return n
    else:
        return -n


print(myAbs(10))


# x作为定参，n可缺省默认2
def power(x, n=2):
    c = 1;
    while n > 0:
        n -= 1
        c = c * x
    return c


print(power(2, 10))


def count(x):
    sum = 0
    for n in x:
        sum += n;
    return sum


print('count=', count([1, 2]))


# * 代表可接受不定个参数，相当于java中的 ...
def count(*x):
    sum = 0
    for n in x:
        sum += n
    return sum


print('count=', count(1, 2, 3, 2.3))

list = [1, 2, 3]
print('list sum=', count(*list))


# 关键字参数 *kw

def persion(name, age, **kw):
    return 'name=%s,age=%d,other=%s' % (name, age, kw)


def persion(name, age, **kw):
    var = kw;
    if 'city' in kw:
        print(kw['city'])
    if 'school' in kw:
        print(kw['school'])
    print('name:', name, 'age:', age, 'other:', kw, '\n')


persion('wuxinxi', 20, city='安徽亳州', school='亳州三中')


# 限制关键字参数名,只接受city、school,但是和位置无关
# 如果想缺省，给定默认值即可 city='亳州'

def persion(name, age, *, city, school):
    return 'name=%s,age=%d,city=%s,school=%s' % (name, age, city, school)


print(persion('wuxinxi', 25, city='亳州', school='亳州第三完全中学'), '\n')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


print(person('wu', 12, 'jh', city='an', job='sz'))

print('\n', '------------------------分界线-------------------------------', '\n')


# 计算1个或多个参数的乘积
def product(x, *s):
    productCnt = x

    for n in s:
        productCnt *= n

    return productCnt


print('乘积结果=', product(1, 2, 3, 4, 5, 6, 7))

print('\n', '------------------------分界线-------------------------------', '\n')


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


print('递归算法：', fact(10),'\n')


# 如果fact(1000)就会出现问题了，栈溢出
# 优化，尾递归，函数返回的时候调用自身本身，返回语句无表达式

def fact(n):
    return fact_iter(n,1)


def fact_iter(n, p):
    if n == 1:
        return p
    return fact_iter(n - 1, n * p)

print('优化后递归算法：',fact(100),'\n')

print('\n', '------------------------分界线-------------------------------', '\n')

def move(n,a,b,c):
    if n==1:
        print(a,'--->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

print(move(4,'A','B','C'))