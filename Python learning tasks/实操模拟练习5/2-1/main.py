#########################################################################
# 任务1：导入必要的类
#########################################################################
# 从指定模块中导入实体类
from entity import Employee,Department
#____【1】____ import Employee, Department



#########################################################################
# 任务2：创建初始的部门和员工对象
# 本任务需要补全Employee类的__str__函数代码空缺
#########################################################################
print('【任务2开始】', '=' * 100)

dept1 = Department(1, '开发部')

emp1 = Employee(1001, 'Jerry', '男',  23.0, dept1)
emp2 = Employee(1002, 'David', '男',  28.0, dept1)
emp3 = Employee(1003, 'Jane', '女',  18.5, dept1)
emp4 = Employee(1004, 'Jessy', '女',  25.0, dept1)

# 输出emp1的信息
print("emp1的信息：", emp1)

print('【任务2结束】', '=' * 100)



#########################################################################
# 任务3：将部门与员工关联
#########################################################################
print('【任务3开始】', '=' * 100)

# 将所有员工加入dept1
for emp in [emp1, emp2, emp3, emp4]:
    dept1.employees.add(emp)#____【4】____)

# 输出dept1部门所有员工信息
print("dept1下所有员工信息：")
dept1.print_employees()#____【5】____()

print('【任务3结束】', '=' * 100)



#########################################################################
# 任务4：根据条件查找匹配的员工信息
#########################################################################
print('【任务4开始】', '=' * 100)
 
# 在dept1部门内查找所有男员工
gender = '男'
results = filter(lambda emp: emp.gender== gender, dept1.employees)
#____【6】____ == gender, dept1.employees)
# 查询结果转换成list
results_list = list(results)#____【7】____(results)
for result in results_list:
    print(result)

# 在dept1部门内查找姓名包含字母'J'的员工
name = 'J'
# 姓名匹配并构造匹配的对象
results = [employee for employee in dept1.employees if name in employee.name]#____【8】____ employee.name]
print("dept1下姓名包含J的员工：")
for result in results:
    print(result)

print('【任务4结束】', '=' * 100)



#########################################################################
# 任务5：根据薪资进行排序
#########################################################################
print('【任务5开始】', '=' * 100)

# 定义按salary进行比较的函数
def compare_by_salary(emp):
    return emp.salary

# 将dept1的员工集合转换成list
employees = list(dept1.employees)
# 根据salary从高到底排序
employees.sort(key=compare_by_salary,reverse=True)#____【9】____, reverse=____【10】____)
for emp in employees:
    print(emp)

print('【任务5结束】', '=' * 100)