# 定义实体类

# 员工类
class Employee(object):
    def __init__(self, empid, name, gender, salary, department):
        self.empid = empid      # 员工编号
        self.name = name        # 员工姓名
        self.gender = gender    # 员工性别
        self.salary = salary    # 员工薪水
        self.dept = department        # 员工所属的部门对象
    
    #########################################################################
    # 任务2相关：创建初始的部门和员工对象
    #########################################################################
    # 以指定的文本格式输出员工的信息
    def __str__(self):
        # 获取所属部门名称(如果没有所属部门，则返回'无部门')
        dept_name = self.dept.name  if self.dept else '无部门'
        # ____【2】____ self.dept ____【3】____ '无部门'
        return "%s, %s, %.2f, %s" % (self.name, self.gender, self.salary, dept_name)


# 部门类
class Department:
    def __init__(self, deptid, name):
        self.deptid = deptid    # 部门编号
        self.name = name        # 部门名称
        self.employees = set()  # 部门下所有员工对象
    
    # 打印输出本部门所有员工信息
    def print_employees(self):
        for employee in self.employees:
            print(employee)