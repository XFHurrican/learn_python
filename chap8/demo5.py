#集合创建方式
s={2,3,4,5,5,6,7,7}
print(s,type(s))

s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,4,5,6])#列表转集合
print(s2,type(s2))

s3=set((1,2,2,3,5,6))#元组转集合
print(s3,type(s3))

s4=set('python')
print(s4,type(s4))
