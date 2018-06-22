
# 读取文件
import  time
import  os
from Include.py.init import Student
import json
import pickle #序列化

filePath='C:/Users/Tangren/Desktop/User.xml'
# filePath='H:/文档\北京/开发使用的文件/特8外/L56008_25008_20150720.lin'
# 读取二进制文件需改为 'rd',追加或者创建'a'

# with open(filePath,'r',) as  f:
#     for line in f.readlines():
#         print(line.strip())

#追加文件，如果不存在先创建
with open(filePath,'a') as f:
    time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    # f.write(time+'时追加信息！\n')
    print(time,'\n')

# ensure_ascii=False显示中文而非ascii
map=dict(name='张三',age=20,add='anhuibozhou')
jsonObject=json.dumps(map,ensure_ascii=False)
print('Json=',jsonObject,'\n')

map=json.loads(jsonObject)
print('map=',map,'\n')



student=Student('wuxinxi','java1305','湖南软件职业学院')

print(json.dumps(student.__dict__,ensure_ascii=False),'\n')
