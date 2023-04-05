s=0#登录次
user=float(input("请创建用户名："))
password=float(input("请创建用户密码："))
input("设置成功！")
#a_user=input("请输入用户名：")
#a_password=input("请输入密码：")
while s<3:
    a_user=float(input("请输入用户名："))
    a_password=float(input("请输入密码："))
    if user==a_user and password==a_password:
        print("登录成功")
        break
    else:
        print("以错误",s+1,"你输入的密码或用户名错误！请重新输入")
    s+=1
    if s==3:
        print("超过三次错误，请稍后重试")
        s+=1
        

