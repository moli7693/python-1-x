class Course:
    number = 0
    name = ""
    teacher = ""
    __location = " "

    def __init__(self, number, name, teacher, location):
        self.number = number
        self.name = name
        self.teacher = teacher
        self. __location = location

    def show_info(self):
        print(f"编号：{self.number}")
        print(f"名称：{self.name}")
        print(f"老师：{self.teacher}")
        print(f"上课地点：{self.__location}")


course_ljw = Course(1, "python", "王璐", "305教室")
course_ljw.show_info()
