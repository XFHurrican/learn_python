#第61课
score={'张三':100,'李四':90,'王五':80}
print('张三' in score)
print('张三' not in score)

del score['张三']
print(score)

score['陈六']=98
print(score)
print(score['李四'])