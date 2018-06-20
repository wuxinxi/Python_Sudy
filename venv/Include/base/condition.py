# 条件
import time
import math

print('请输入您的年龄：')

inputStr = input();

age = int(inputStr)

print('您输入的年龄是：', age, ',请稍后……')

time.sleep(0.5)

if age >= 18:
    print('您已成年^_^')
    print('欢迎使用本产品!')
else:
    print('年龄不符！！！')
    print('正在退出……')
    time.sleep(0.3)
    print('退出成功！')

print('--------------------分界线--------------------')

height = 17.5
weight = 80.5

bmi = weight / math.sqrt(height)

bmiEnd = round(bmi, 2)
print('BMI:', bmiEnd)

if bmiEnd <= 18.5:
    print(bmiEnd, ',过轻')
elif 18.5 < bmiEnd < 25:
    print(bmiEnd, ',正常')
elif 25 < bmiEnd < 28:
    print(bmiEnd, ',过重')
elif 28 < bmiEnd < 32:
    print(bmiEnd, ',肥胖')
elif 32<bmiEnd:
    print(bmiEnd, ',严重肥胖')
