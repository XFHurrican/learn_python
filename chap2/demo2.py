#转义字符
# \n new line 换行
# \r return 回车
# \t tab 水平制表符
# \b backspace 退格
print('hello\nworld')
print('hello\tworld')
print('hello\rworld')
print('hello\bworld')
print('http://www.baidu.com')
print('http:\\www.baidu.com')
print('老师说:\'大家好\'')
#不希望字符串中转义字符起作用，在字符串前加r
print(r'hello\nworld')