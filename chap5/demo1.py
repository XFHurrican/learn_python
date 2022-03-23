#第35课
#range的三种创建方式
r=range(10)     #默认0开始，相差1
print(r)
print(list(r))

r=range(1,10)
print(list(r))

r=range(1,10,2)
print(list(r))

print(10 in r)
print(9 in r)

print(10 not in r)
print(9 not in r)
