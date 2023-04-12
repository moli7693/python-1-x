#########################################################################
# 任务1：实现一维数组的冒泡法排序(升序)
#########################################################################
print('【任务1开始】', '=' * 100)

# 冒泡排序法升序排列一维数组
def sort_bubble(arr):
    length = len(arr)#____【1】____(arr)
    for i in range(0, length - 1):
        print(i,end=" ",)
        for j in range(i + 1,length):#____【2】____, length):
            print(j,end=" ")
            # 比较前后两个数的大小
            if arr[j] <arr[i]:#____【3】____ arr[i]:  
                # 交换两个数 
                temp = arr[j]#____【4】____]
                arr[j] = arr[i]
                arr[i] = temp

arr1 = [100, 3, 5, 8, 20, 100, 8, 34, 67, 3]
arr2 = arr1.copy()
sort_bubble(arr1)
print("自定义冒泡排序结果：", arr1)

result = arr2.sort()
print("调用库函数排序结果：", arr2)

print('【任务1结束】', '=' * 100)


#########################################################################
# 任务2：计算给定字符串中数字、大写和小写字母的数量
#########################################################################
print('【任务2开始】', '=' * 100)

num_digit = 0       # 记录数字字符个数
num_capital = 0     # 记录大写字符个数
num_lowercase = 0   # 记录小写字符个数

str = 'Hello Python from 1990!'
for c in str:
    if c.isdigit():#____【5】____():
        num_digit += 1
    elif c.islower():
        num_lowercase += 1
    elif c.isupper():#____【6】____():
        num_capital += 1

print("数字个数%d, 大写字符个数%d, 小写字符个数%d"
    %(num_digit, num_capital, num_lowercase))


print('【任务2结束】', '=' * 100)