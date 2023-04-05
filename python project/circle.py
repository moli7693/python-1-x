try:
    circle_a = float(input("请输入圆的半径:"))
except ValueError:
    print("请输入数字！")
else:
    if circle_a <= 0:
        print("请输入0/负数除外的数字")
    else:
        circle = 3.14*circle_a*circle_a
        print(f"圆的面积为:{circle}")
