#第100课
try:
    a=int(input('请输入第一个数：'))
    b=int(input('请输入第二个数：'))
    div=a/b
    print('结果为：',div)
except ZeroDivisionError:
    print('除数不能为零')