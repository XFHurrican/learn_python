def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)

lst=[11,22,33]
fun(*lst)

fun(a=100,c=300,b=200)

dic={'a':111,'b':222,'c':333}
fun(**dic)