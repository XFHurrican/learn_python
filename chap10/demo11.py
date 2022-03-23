#斐波那契数列
def fun(a):
   if a==1:
       return 1
   elif a==2:
         return 1
   else:
        b=fun(a-1)+fun(a-2)
        return b



a=int(input('请输入斐波那契数列位数：'))
for i in range(1,a+1):
    print(fun(i),end='\t')

