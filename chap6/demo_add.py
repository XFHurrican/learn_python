#第52课
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))

lst2=['hello','world']
#lst.append(lst2)    #将lst2作为一个元素添加到列表末尾
#print(lst)
lst.extend(lst2)
print(lst)

lst.insert(1,90)
print(lst)

lst3=[True,False,'hello']
lst[1:]=lst3
print(lst)
