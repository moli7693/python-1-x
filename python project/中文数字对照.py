cn = tuple("点壹贰叁肆伍陆柒捌玖")
while True:
        num_a = tuple(input('请输入数字：'))
        try:        #检测异常
            for i in num_a:
                if(i=='.'):
                    i=0
                else:
                    i=int(i)
                print(cn[i], end='')
            break
        except:     #执行发生异常时的代码
            print('您输入的不是数字,请重新输入!')