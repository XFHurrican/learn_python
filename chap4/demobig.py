#第33课
num_a=int(input('请输入第一个整数a：'))
num_b=int(input('请输入第二个整数b：'))
if num_a>num_b:
    print(num_a,'大于',num_b)
elif num_a==num_b:
    print(num_a,'等于',num_b)
else:
    print(num_a,'小于',num_b)

#使用条件表达式进入比较
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))