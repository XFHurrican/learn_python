for item in range(3):
    pwd='xufanghao123'
    if input('请输入密码：')==pwd:
        print('密码正确')
        break
    else:
        print('密码错误')
        if item==2:
            print('三次机会用完')