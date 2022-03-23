#第65课
#字典生成式
items=['Fruits','Books','Others']
prices=[96,78,85]

d={a:b for a,b in zip(items,prices)}
m=dict(zip(items,prices))
print(d)
print(m)