# 定义变量
s = 3       # 设置登录次数
# 设置账号密码
user = input('请设置账号：')
password = input('请设置密码：') 
print('已注册成功！')      
while True:
    # 带提示语输入赋值
    a_user = input('请输入账号：')
    a_password = input('请输入密码：')
    # 登陆成功
    if user == a_user and password == a_password:
        print('登录成功！')
        break
    # 账号密码错误
    else:
        print('账号和密码错误！', end='')
        if s != 1:
            print('还有{}次机会'.format(s - 1))
    # 结束条件
    if s <= 1:
        print('\n输入次数过多,账号已被冻结！')
        break
    s -= 1      # 记录输入次数
 