#第42课
pwd='xufanghao123'
for item in range(3):
    if pwd==input('请输入密码:'):
        print('密码正确')
        break
    else:
        print('密码错误')

else:print('三次机会用完')