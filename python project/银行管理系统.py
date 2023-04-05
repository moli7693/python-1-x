import random
bank_system = [{"姓名":"root","身份证号":"000000000000000000","手机号":"000000","银行卡号":"000000","密码":"000000","余额":2.0,"状态":"正常"}]

# 管理员账号和密码:
root_name = "root"
root_password = "root"

# name 姓名
# ID_number 身份证号
# phone_number 手机号
# password 密码
# amount 余额
# Bank_number 银行卡号

class Bank_registration:
    def __init__(self,name,ID_number,phone_number,password,amount):
            Bank_number = str("")
            while True:
                a = str(random.randint(0,9))
                Bank_number = Bank_number+a
                if(len(str(Bank_number)) == 6):
                    if Bank_number not in bank_system:
                        print(f"您的银行卡号为:{Bank_number},请保存好")
                        bank_system.append({"姓名:":name,"身份证号":ID_number,"手机号":phone_number,"银行卡号":Bank_number,"密码":password,"余额":amount,"状态":"正常"})
                        break
class Bank:
    def inquire(self):
        i = 0
        for e in bank_system:
            if Bank_number_2 == e["银行卡号"]:
                if e["状态"] == "正常":
                    for q in range(3):
                        i += 1
                        password_2 = input("请输入您的密码:")
                        if password_2 == e["密码"]:
                            print("您的余额为:",e["余额"])
                            break
                        elif i == 3:
                            print("密码输入错误3次,账户已被锁定")
                            e.update({"状态":"锁定中"})
                        else:
                            print("您的密码错误,请重新输入")
                            continue
                else:
                    print("您的账户属于锁定中,无法查询,请解锁之后才能查询")
            
    def withdraw(self):
        i = 0
        for e in bank_system:
            if Bank_number_3 == e["银行卡号"]:
                if e["状态"] == "正常":
                    for q in range(3):
                        i += 1
                        password_3 = input("请输入您的密码:")
                        if password_3 == e["密码"]:
                            print("您的余额为:",e["余额"])
                            bank_withdraw = float(input("请输入您要取款的金额:"))
                            if bank_withdraw > e["余额"]:
                                print("您的余额不足!!!")
                            elif bank_withdraw < 0:
                                print("取款金额异常!!!")
                            else:
                                e["余额"] = e["余额"] - bank_withdraw
                                print("取款成功!!!")
                            break
                        elif i == 3:
                            print("密码输入错误3次,账户已被锁定")
                            e.update({"状态":"锁定中"})
                        else:
                            print("您的密码错误,请重新输入")
                            continue
    def deposit(self):
        i = 0
        for e in bank_system:
            if Bank_number_4 == e["银行卡号"]:
                if e["状态"] == "正常":
                    for q in range(3):
                        i += 1
                        password_4 = input("请输入您的密码:")
                        if password_4 == e["密码"]:
                            print("您的余额为:",e["余额"])
                            bank_deposit = float(input("请输入您要存款的金额:"))
                            if bank_deposit < 0:
                                print("存款金额异常!!!")
                            else:
                                e["余额"] = e["余额"] + bank_deposit
                                print("存款成功!!!")
                            break
                        elif i == 3:
                            print("密码输入错误3次,账户已被锁定")
                            e.update({"状态":"锁定中"})
                        else:
                            print("您的密码错误,请重新输入")
                            continue
                else:
                    print("您的账户属于锁定中,无法查询,请解锁之后才能查询")
    def transfer(self):
        i = 0
        for e in bank_system:
            if Bank_number_5_1 == e["银行卡号"]:
                if e["状态"] == "正常":
                    for q in range(3):
                        i += 1
                        password_5 = input("请输入您的密码:")
                        if password_5 == e["密码"]:
                            bank_transfer = float(input("请输入要转账的金额:"))
                            if bank_transfer >= e["余额"]:
                                judge = input(f"您确认要向账户{Bank_number_5_2}转账{bank_transfer}吗?(yes/no):")
                                if judge == "yes":
                                    e["余额"] = e["余额"] - bank_transfer
                                    for i in bank_system:
                                        if Bank_number_5_2 == e["银行卡号"]:
                                            i["余额"] = i["余额"] + bank_transfer
                                    print("已转账成功!!!")
                                elif judge == "no":
                                    break
                                else:
                                    print("无效操作!!!")
                            elif bank_transfer <= 0:
                                print("转账金额必须大于0")
                            else:
                                print("您的余额不足！！！")
                        elif i == 3:
                            print("密码输入错误3次,账户已被锁定")
                            e.update({"状态":"锁定中"})
                        else:
                            print("您的密码错误,请重新输入")
                            continue
                else:
                    print("您的账户属于锁定中,无法查询,请解锁之后才能查询")
    def lock(self):
        for e in bank_system:
            if Bank_number_6 == e["银行卡号"]:
                if password_6 == e["密码"]:
                    e.update({"状态":"锁定中"})
                else:
                    print("密码错误!!!")
            else:
                print("没有查询到该卡号")
    def deblocking(self):
        for e in bank_system:
            if Bank_number_7 == e["银行卡号"]:
                if password_7 == e["密码"]:
                    e.update({"状态":"正常"})
                else:
                    print("密码错误!!!")
            else:
                print("没有查询到该卡号")
    def preserve(self):
        preserve_8 = open("E:\偷偷内卷\Python学习\银行管理系统数据.txt","a",encoding="UTF-8")
        for e in bank_system:
            for i,m in e.items():
                preserve_8.write(f"{i}:{m}\n")
        preserve_8.close()

while True:
    print("""
    =====================
    银行管理系统
    1.开户
    2.查询
    3.取款
    4.存款
    5.转账
    6.锁定
    7.解锁
    8.存盘
    9.退出
    =====================
    """)
    select = int(input("请选择您想选择的内容(1~9):"))
    if select == 1:
        select_1_name = str(input("请输入用户姓名:"))
        select_1_ID_number = str(input("请输入身份证号:"))
        if len(select_1_ID_number) == 18:
            select_1_phone_number = str(input("请输入手机号:"))
            select_1_amount = float(input("请输入预留金额:"))
            try:
                select_1_password = int(input("请设置银行卡密码:"))
                if len(str(select_1_password)) !=6:
                    print("银行卡密码只能是6位,请重新输入")
                    continue
            except ValueError:
                print("输入的密码不是纯数字")
                continue
            else:
                select_1_password = str(select_1_password)
                bank = Bank_registration(select_1_name,select_1_ID_number,select_1_phone_number,select_1_password,select_1_amount)
                print("已开户成功!!!")
        else:
            print("身份证号非18位,请重新输入!!!")
    elif select == 2:
        bank = Bank()
        Bank_number_2 = input("请输入卡号:")
        bank.inquire()
    elif select == 3:
        bank = Bank()
        Bank_number_3 = input("请输入卡号:")
        bank.withdraw()
    elif select == 4:
        bank = Bank()
        Bank_number_4 = input("请输入卡号:")
        bank.deposit()
    elif select == 5:
        bank = Bank()
        Bank_number_5_1 = input("请输入转出卡号:")
        Bank_number_5_2 = input("请输入转入卡号:")
        bank.transfer()
    elif select == 6:
        bank = Bank()
        Bank_number_6 = input("请输入卡号:")
        password_6 = str(input("请输入密码"))
        bank.lock()
    elif select == 7:
        bank = Bank()
        Bank_number_7 = input("请输入卡号:")
        password_7 = str(input("请输入密码"))
        bank.deblocking()
    elif select == 8:
        bank = Bank()
        # 文件地址视情况而定
        bank.preserve()
        print("已将用户信息保存")
    elif select == 9:
        root_name_1 = input("请输入管理员账号:")
        root_password_1 = input("请输入管理员密码:")
        if root_name_1 == root_name and root_password_1 == root_password:
            bank.preserve()
        else:
            print("管理员账号或者密码错误,请重新输入!!!")
            continue
        print("拜拜~")
        break
    else:
        print("选择的内容异常,请重新选择!!!")