from cmath import inf


ticket=input("是否购买车票（输入是或否）：")
if ticket=='是':
    safe=input("是否持有管制刀具，请输入刀具长度（cm）:")
    if safe<10:
        print("请进站")
    else:
        print("不允许进站")
else:
    print("请先购买车票")