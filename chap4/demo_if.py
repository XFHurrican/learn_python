#第29课
money=1000
s=int(input('请输入取款金额：'))
if s<=money:
    money=money-s
    print('取款成功，余额为：',money)