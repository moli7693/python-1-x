import math
class BianError(Exception):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
try:
    a=int(input("请输入第一条边:"))
    b=int(input("请输入第二条边:"))
    c=int(input("请输入第三条边:"))
    if a+b<c or a<c-b or b+c<a or b<a-c or a+c<b or c<b-a or a+b==c:
        raise BianError(a,b,c)
except BianError as result:
    print(f"三变不合法,三边为{result.a} {result.b} {result.c}")
except ValueError:
    print("请输入数字！")

else:
    zhouchang=a+b+c
    s=(zhouchang)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("周长为:{:.2f},面积为:{:.2f}".format(zhouchang,area))
    