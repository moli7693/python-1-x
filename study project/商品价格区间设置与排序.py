num=[399,4369,539,288,109,749,235,190,99,1000]
a=int(input("请输入最大价格："))
b=int(input("请输入最小价格："))
c=input('''1.价格降序排序
2.价格升序排序
请选择序号：''')
#num1=[]
#for i in num:
   # if i >= b and i<=a:
 #      num1.append(i)     
#if c=='1':
   # d=sorted(num1,reverse=True)
   # print(d)
#if c=='2':
 #   num1.sort()
  #  print(num1)
num[a:b:]
if c=='1':
    d=sorted(num,reverse=True)
    print(d)
if c=='2':
    num.sort()

