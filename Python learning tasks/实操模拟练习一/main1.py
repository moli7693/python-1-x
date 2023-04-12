#########################################################################
# 任务1：使用递归调用实现Fibonacci函数
#########################################################################
import time
print('【任务1开始】', '=' * 100)

# 以递归方式实现的函数


def fibonacci_recursive(num):
    if num <= 2:
        return 1  # ____【1】____
    # ____【2】____)
    return fibonacci_recursive(num - 1) + fibonacci_recursive(num-2)


# 以循环方式实现的函数
def fibonacci_traversive(num):
    # 初始化，第1、2个Fibonacci数的值都为1
    temp1 = temp2 = 1
    # 从第3个元素开始，依次根据前2个元素值，计算后1个元素的值
    for i in range(3, num + 1):
        temp = temp1 + temp2      # 计算前两个数之和
        temp1 = temp2  # ____【3】____   # temp1和temp2分别更新赋值
        temp2 = temp
    # 返回第num个元素的计算结果
    return temp2


# 用两种方式分别计算Fibonacci序列前10个元素的值
for i in range(1, 11):  # ____【4】____):
    print("第%d个元素值为：%d, %d" %
          (i, fibonacci_traversive(i), fibonacci_recursive(i)))

print('【任务1结束】', '=' * 100)


#########################################################################
# 任务2：粗略计算函数运行的时间
#########################################################################
print('【任务2开始】', '=' * 100)


# 计算Fibonacci指定元素值并统计运行耗时
# func：传入的函数，本例中可传入递归调用fibonacci_recursive或循环调用fibonacci_traversive的函数
# num：传入待计算的第num个元素
# 返回值：Fibonacci计算结果，函数运行耗时

def test_fibonacci(func, num):
    start = time.time()     # 记录函数调用初始时间戳
    result = func(num)  # ____【5】____(num)      # 调用函数
    end = time.time()       # 记录函数调用结束时间
    # 返回计算结果和耗时
    return (result, end - start)  # ____【6】_______


# 通过test_fibonacci分别调用递归和循环函数，输出计算结果和耗时
num = 38        # 计算Fibonacci中第num个元素的值
print("计算Fibonacci序列第%d个元素的值并衡量耗时......" % num)
result, t = test_fibonacci(fibonacci_recursive, num)
print("递归调用，结果为：%d， 耗时：%.4f秒" % (result, t))
result, t = test_fibonacci(fibonacci_traversive, num)
print("循环调用，结果为：%d， 耗时：%.4f秒" % (result, t))

print('【任务2结束】', '=' * 100)
