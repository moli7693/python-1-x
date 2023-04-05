class Circle:
    radius = ''
    Π = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        # 圆的周长
        circlr_l = 2*(self.radius*self.Π)
        print(f"圆的周长为：{circlr_l}")

    def get_area(self):
        circle_s = self.Π*(self.radius*self.radius)
        print(f"圆的面积:{circle_s}")


circle_ls = Circle(2)
circle_ls.get_perimeter()
circle_ls.get_area()
