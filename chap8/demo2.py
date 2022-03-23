#第67课
t=('python','world',98)
print(t)
print(type(t))

t1=tuple(('python','world',98))
print(t1)
print(type(t1))

t2='python','world',98
print(t2)
print(type(t2))

#空元组，空列表的创建方式
lst=[]
lst1=list()

d={}
d1=dict()

t4=()
t5=tuple()

print('空列表',lst,lst1)
print('空字典',d,d1)
print('空元组',t4,t5)