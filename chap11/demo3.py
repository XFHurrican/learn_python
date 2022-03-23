lst=[{'rating':9.7,'type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['蒂姆罗宾斯','摩根弗里曼']},
     {'rating':9.6,'type':['爱情','剧情'],'title':'霸王别姬','actors':['张国荣','葛优']},
     {'rating':9.6,'type':['爱情','剧情'],'title':'阿甘正传','actors':['汤姆汉克斯','罗宾']}]

name=input('请输入你要查询的演员：')
for item in lst:
    if name in item['actors']:
        print(item['title'],item['rating'],'\n',item['type'])


