def fun(a,b=10):
    print(a,b)

def fun1(*args):
    print(args)

def fun2(**args):
    print(args)

def fun4(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
fun(12)
fun1(11,22,33)
fun2(a=1,b=2,c=3)
fun4(1,2,3,4)
fun4(d=1,c=3,b=2,a=1)