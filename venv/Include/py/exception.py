# 异常、错误捕获

import logging
logging.basicConfig(level=logging.DEBUG)


class comp(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise comp('invalid value %s'% s)
    return 10/n

foo('1')

try:
    print('开始计算……')
    logging.info('开始计算……')
    var=10/1
    logging.info('计算结果:%d'% var)
    print('计算结果')

except Exception as e:
    print('异常提示：',e)
    logging.exception(e)

finally:
    print('结束……')



from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        print('Error:',e)
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
