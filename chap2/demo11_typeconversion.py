#第16课
name='张三'
age=20

print(type(name),type(age))
#print('我叫'+name+'今年'+age+'岁')#int型与str型连接时报错
print('我叫'+name+'今年'+str(age)+'岁')

#str()将其他类型转换为str型
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

#int()将其他类型转化为int型
s1='128'
f1=98.7
s2="76.77"
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))#将str转为int,字符串为数字串
print(int(f1),type(int(f1)))#将float转为int，舍弃小数部分
#print(int(s2),type(int(s2)))
print(int(ff),type(int(ff)))
print(int(s3),type(int(s3)))#将str转为int型，字符串必为数字串，且必为整数