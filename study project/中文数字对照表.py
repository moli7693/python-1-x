numbers = ('零壹贰叁肆伍陆柒捌玖')
number=input("输入一个数字:")
number1=number.replace('.','d')
number2=list(number1)
print(number2)
for i in number2:
    if i=='d':
        number2.remove('d')  
        print(number2)
        for b in number2:
            print(numbers[int(b)],end="")

