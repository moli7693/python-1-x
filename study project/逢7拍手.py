for i in range(1, 101):
    if i % 7 == 0 or '7' in str(i):
        print('*', '', end='')
    else:
        print(i, '', end='')
    #if i % 10 == 0:
           # print('\r')
