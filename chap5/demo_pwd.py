#第40课
#从键盘录入密码，最多录入三次,正确则结束循环
code='xufanghao123'
i=1
while i<=3:
    if input('请输入密码：')==code:
        print('密码正确')
        break
    else:
        print('密码错误')
    i+=1
if i>3:
    print('三次机会用完')
