for item in range(100,1000):
    if (item//100)**3+((item//10)%10)**3+(item%10)**3==item:
        print(item)