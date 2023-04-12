# main1 模拟题说明

def fibonacci_recursive(num):
    if num <= 2:
        return 1  # ____【1】____
    # ____【2】____)
    return fibonacci_recursive(num - 1) + fibonacci_recursive(num-2)

 if num <= 2:
        return 1  # ____【1】____
    # ____【2】____)
   判断num是否<=2，如果<=2返回1
   return fibonacci_recursive(num - 1) + fibonacci_recursive(num-2)
   递归计算 num的值 当num的值 num <= 2则返回递归的值

def fibonacci_traversive(num):
    # 初始化，第1、2个Fibonacci数的值都为1
    temp1 = temp2 = 1
    # 从第3个元素开始，依次根据前2个元素值，计算后1个元素的值
    for i in range(3, num + 1):
    num+1 是for循环的次数如果
        temp = temp1 + temp2      # 计算前两个数之和
        temp1 = temp2  # ____【3】____   # temp1和temp2分别更新赋值
        temp2 = temp
    # 返回第num个元素的计算结果
    return temp2



