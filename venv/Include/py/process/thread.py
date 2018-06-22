import time
import threading

def loop():

    print('线程 %s 正在运行……>>1>>' % threading.current_thread().name)

    n=0;
    while n<3:
        n+=1

        print('线程 %s循环第 %s 次' % (threading.current_thread() ,n))
        time.sleep(2)

    print('循环结束……')


t=threading.Thread(target=loop,name='LoopThrad')
# t.start()
# print('线程 %s 正在运行……>>3>>' % threading.current_thread().name)


balance=0

def change_balance(m):
    global  balance
    balance=balance+m
    balance=balance-m


def run_thread(n):
    for i in range(2500000):
        change_balance(i)


t1=threading.Thread(target=run_thread,args=(5,))

t2=threading.Thread(target=run_thread,args=(8,))


t1.start()
t2.start()
t1.join()
t2.join()

print(balance)