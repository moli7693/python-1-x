def fibonacci(n):
    # 使用 for 循环实现斐波那契数列
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


fibonacci(10)
