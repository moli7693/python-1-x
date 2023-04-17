
from random import randint, random
import random

monky=int(input("请输入树上猴子："))
oldmonky=int(input("请输入地上几个猴子："))
print("让我猜一猜一共几个猴子")
monkeys=monky+oldmonky
number=random.randint(1,20)
if monkeys==number:
    print("nmsl?知道几只猴还问我")
elif monkeys in[10,14,14,56,12]:
        print("我不认识数！",number+2,"猴？")
elif monkeys<=number:
        print("猴见到你跑了！！！！")
elif monkeys>number:
    print("你是fw吗？让我数？")
elif number<monkeys<(number+1):
    print("hjb666")


