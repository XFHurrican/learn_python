answer=input('是否是会员？')
price=int(input('购买商品价格:'))
if answer=='是':
    if price>=200:
        print(price*0.8)
    elif 100<=price<=200:
        print(price*0.9)
    else:
        print(price)
else:
    if price>=200:
        print(price*0.95)
    else:
        print(price)