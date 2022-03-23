t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
print(id(t[1]))

t[1].append(100)
print(t)
t[1].insert(1,10)
print(t)
print(id(t[1]))

s=[1,2,3]
print(id(s))
s1=s
print(id(s1))