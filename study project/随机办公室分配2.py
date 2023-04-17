import random   
j=0
i=0    
# 定义一个空的嵌套列表，充当一个学校，有三个办公室
office = [[], [], []]
teacher=['俊博','小武','燕六','李二','张二','王五','李四','张三']
for a in teacher:
    s=random.randint(0,2)
    office[s].append(a)
i=1
while i<len(office):
    for  o in office:
        print(f'{i}号办公室的人数{len(office)},老师有：')
    #打印办公室人数——子列表数据个数 len()
        for a in o:
            print(a)
            i+=1








#for i in teacher:
   # s = random.randint(0, 2)    # 从0-2之间产生一个随机数
   # office[s].append(i)
#i=1
#for o in office:
 #   print('办公室',i,'的人数是',len(o),'老师分配是：')
  #  for a in o:
   #     print(a)
    #i += 1