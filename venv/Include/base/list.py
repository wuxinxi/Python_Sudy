# list 集合

names = ['唔系想你', 'haha', '666', '测试']

names.append("tom2")

for name in names:
    print(name)

print('长度：', len(names))

print('------------分界线------------')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print("apple:", L[0][0])

print('python:', L[1][1])

print('LisaL:', L[2][2])

print('----------------分界线----------------')
# for in 循环
sum = 0
for x in [0, 2, 5, 10, 88, 45]:
    sum += x;
print('计算结果:', sum)

# range(num) 范围
numList = range(101)
count = 0
for num in numList:
    count += num;
print('5050:', count)

# while 循环

whileList = range(10)
length = len(whileList)
print ('长度：',length)

cnt = 0;
while cnt<length:
    print(whileList[cnt])
    cnt+=1

print("退出")


print('----------------------------------------','\n')

L = ['Bart', 'Lisa', 'Adam']

for n in L:
    print(n,'\n')

# 取值定索引
print('range','----------------------------------------')

# range (最笨的方法)
for n in range(2):
    print(L[n])

# 切片 slice

print('slice','----------------------------------------')
print('切片slice',L[1:2],'\n')# 即从索引1开始取到索引2，但不包括2


li=['A','B','C','D']
print(li,li[:3],'\n')

listRange=list(range(100))
print(listRange[::2],'\n')# 所有的数每2个取一个

# 甚至字符串都可以使用切片
var='ABCDEFGHIJKL'
print(var[-1:])

# 因此切片slice另外一个用处就是字符串的截取

print('----------------','去除首尾空格--------------------','\n')

def trim(str):
    if len(str)==0:
        return
    else:
        if str[:1]==' ':
            return trim(str[1:])

        if str[-1:]==' ':
            return str[:-1]

        return str

print(trim(' Hello '))



print('\n','---------------列表生成式------------------')

# 生成1-20的列表
range1_20=list(range(1,21))
print(range1_20,'\n')

# 如果想生成1*2,2*2,3*2 ……这种类型的呢

# 1.循环
L=[]
for x in range(1,21):
    L.append(x*2)

print('方法1：',L,'\n')

# 2.列表生成式的方式
L2=[ x*2 for x in range(1,21)]
print('方法2：',L2,'\n')


print('\n','---------------列出所有文件------------------')

import  os

listDri=[d for d in os.listdir('.')]
print(listDri,'\n')


Name= ['Hello', 'World', 'IBM', 'Apple']

# 全部转成小写
Name_lower=[s.lower() for s in Name]

# 全部转换成大写
Name_upper=[s.upper() for s in Name]

print('原始 数据:',Name)
print('转换成小写:',Name_lower)
print('转换成大写:',Name_upper)


print('\n','---------------作业------------------')

# 将L1 转换成小写的（注意不合法类型）

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if(isinstance(s,str))]

print('原始数据:',L1)
print('转换后数据：',L2)



print('\n','---------------生成器generator------------------')
L=[x*x for x in range(1,11)]

lg=(x*x for x in range(1,11))

print(L,'\n')
# for x in lg:
#     print(x)


L1 = ['adam', 'LISA', 'barT']

def normalize(name):
    return name[0].upper()+name[1:].lower()

L2=list(map(normalize,L1))
print(L2)


def is_odd(n):
    return n%2==0


numList=list(range(1,101))
filterList=list(filter(is_odd,numList))

print(filterList)


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
# [1:10:2] 从1开始，前10个，每2个取一个

def number_of_times(n):
    n=str(n)
    return n[::1]==n[::-1]

Li=list(range(1,1000001))

filterLi=list(filter(number_of_times,Li))
print(filterLi)

