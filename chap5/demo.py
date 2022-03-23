#第43课
for i in range(1,10):
    for j in range(1,10):
        print(j,'*',i,'=',j*i,end='\t')
        if j==i:
            print('\n')
            break