try:
    a=int(input('请输入被除数：'))
    b=int(input('请输入除数：'))
    div=a/b
except BaseException:
    print('出错了')
else:
    print('结果为：',div)
finally:
    print('谢谢您的使用')