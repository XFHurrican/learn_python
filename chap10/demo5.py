#第91课
def fun(*args):
    print(args)

fun(1,2,3)
fun(10)

def fun1(**args):
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)