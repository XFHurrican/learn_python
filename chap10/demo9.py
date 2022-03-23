def fac(a):
    if a==1:
        return 1
    elif a>1:
        return a*fac(a-1)
    elif a==0:
        return 1

a=int(input('阶乘：'))
print(fac(a))