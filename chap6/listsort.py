#第55课
lst=[20,40,10,98,54]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)  #reverse=True为降序排序
print(lst)
lst.sort(reverse=False) #reverse=False为升序排序
print(lst)
print('-----------------使用内置函数sorted(),产生一个新的列表对象——————————————————')
lst=[20,40,10,98,54]
print(lst)
new=sorted(lst)
print(lst)
print(new)
print('-----------------指定关键字参数----------------')
desc_list=sorted(lst,reverse=True)
print(desc_list)
incre_list=sorted(lst,reverse=False)
print(incre_list)