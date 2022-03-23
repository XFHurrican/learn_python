#第23课
a,b=10,20
print('a大于b吗?',a>b)
print('a小于b吗?',a<b)
print('a等于b吗?',a==b)
print('a不等于b吗?',a!=b)

a=10
b=10
print(a==b)
print(a is b)

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)   #True

lst1=[11,22,33,44]
lst2=[11,22,33,43]
print(lst1==lst2)   #False

print(a is not b)
print(lst1 is not lst2)