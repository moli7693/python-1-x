import random

# 开户的异常定义


class IdCardExceptin(Exception):  # 自定义身份证异常
    def __init__(self, length):
        self.length = length  # 最大长度


class PhoneExceptin(Exception):  # 自定义身份证异常
    def __init__(self, length):
        self.length = length  # 最大长度


class PassWdExceptin(Exception):  # 自定义身份证异常
    def __init__(self, length):
        self.length = length  # 最大长度


class Printuser():
    def atmview(self):
        print("**********************************************")
        print("*           开户（1）     查询（2）             *")
        print("*           存款（3）     取款（4）             *")
        print("*           转账（5）     锁定（6）             *")
        print("*           存盘（7）     解锁（8）             *")
        print("*                   退出（0）                 *")
        print("**********************************************")


# 开户信息
user = []
Data = {}


class Bank:
  # 存储用户信息！

    def CreatUser(self):
        while True:
            name = input("请输入您的姓名：")
            try:
                idCard = input("请输入您的身份证号：")
                if len(idCard) != 18:  # 判断身份证号是否是18位
                    raise IdCardExceptin(len(idCard))
            except IdCardExceptin as result:
                print(f"身份证错误！！！！,你输入的长度为{result.length}身份证号码应当18位")
                continue
            else:
                try:
                    phone = input("请输入您的电话号码：")
                    if len(phone) != 11:  # 判断是否是11位
                        raise PhoneExceptin(len(idCard))
                except PhoneExceptin as result:
                    print(f"你输入的手机号错误,应当11位,你输入的长度为{result.length}")
                    continue
                else:
                    try:
                        Passwd = input("请输入密码：")
                        if len(Passwd) != 6:  # 判断是否是6位
                            raise PassWdExceptin(len(Passwd))
                    except PassWdExceptin as result:
                        print(f"你输入的密码错误,应当11位,你输入的长度为{result.length}")
                        continue
                    else:
                        cardid = str(random.randint(
                            100000, 999999))  # 随机生成六位数卡号
                        preMoney = float(input("请输入您的预存款金额："))
                        if preMoney < 0:
                            print("预存款输入有误，开户失败......")
                            return -1
    # card = Card(cardid, Passwd, preMoney)
    # user = User(name, idCard, phone, card)
                        Data = {}
                        Data["Passwd"] = Passwd
                        Data["preMoney"] = preMoney
                        Data["name"] = name
                        Data["idCard"] = idCard
                        Data["phone"] = phone
                        Data["carid"] = cardid
                        user.append(Data)
                        print("开户成功，请牢记卡号:(%s)" % cardid)
                        break

# 查询账户信息
    def SerchUser(self):  # 判断银行卡号是否错误3次然后锁定银行账户
        cardnum = input("请输入您的卡号：")
        for e in user:  # 遍历user用户列表
            if cardnum == e["carid"]:  # 判断卡号是否在字典中！！
                count = 0
                while count < 3:  # 判断是否超过3次
                    passwd = input("请输入密码:")
                    if passwd == e["Passwd"]:
                        print("————账户信息————")
                        print(f"姓名:{e['name']}")
                        print(f"余额:{e['preMoney']}")
                        return
                    else:
                        count += 1
                        print(f"输入错误你还有{3-count}次机会！！！")
                print("输入密码超过三次错误，你的账户已被锁定！！")
                Data["onoff"] = "off"  # 向用户字典中添加被锁定信息！！！
                user.append(Data)
                return
            else:
                print("你的银行卡号错误！！！")
# 存款！！

    def Cunkuan(self):
        cardnum = input("请输入您的卡号：")
        for e in user:  # 遍历user用户列表
            if cardnum == e["carid"]:  # 判断卡号是否在字典中！！
                count = 0
                while count < 3:  # 判断是否超过3次
                    passwd = input("请输入密码:")
                    if passwd == e["Passwd"]:
                        try:
                            cunkuan = float(input("请输入存款:"))
                            if cunkuan > 0:
                                e["preMoney"] = float(e["preMoney"]+cunkuan)
                                return
                            else:
                                print("存款不能为0")
                        except ValueError:
                            print("请输入数字")
                    else:
                        count += 1
                        print(f"输入错误你还有{3-count}次机会！！！")
                print("输入密码超过三次错误，你的账户已被锁定！！")
                Data["onoff"] = "off"  # 向用户字典中添加被锁定信息！！！
                user.append(Data)
                return
            else:
                print("你的银行卡号错误！！！")
# 取款

    def QuKan(self):
        cardnum = input("请输入您的卡号：")
        for e in user:  # 遍历user用户列表
            if cardnum == e["carid"]:  # 判断卡号是否在字典中！！
                count = 0
                while count < 3:  # 判断是否超过3次
                    passwd = input("请输入密码:")
                    if passwd == e["Passwd"]:
                        try:
                            # 异常处理判断是否存款0元或者添加了数字
                            cunkuan = float(input("请输入存款:"))
                            if cunkuan > 0:
                                e["preMoney"] = float(e["preMoney"]-cunkuan)
                                return
                            else:
                                print("存款不能为0")
                        except ValueError:
                            print("请输入数字")
                    else:
                        count += 1
                        print(f"输入错误你还有{3-count}次机会！！！")
                print("输入密码超过三次错误，你的账户已被锁定！！")
                Data["onoff"] = "off"  # 向用户字典中添加被锁定信息！！！
                return
            else:
                print("你的银行卡号错误！！！")

    def ZhuanZhang(self):
        cardnum = input("请输入您的卡号：")
        for e in user:  # 遍历user用户列表
            if cardnum == e["carid"]:  # 判断卡号是否在字典中！！
                a_card = input("请输入需要转账的用户的卡号:")
                if a_card != e["carid"]:
                    print("你转账的用户不存在")
                    return
                else:
                    a_money = float(input("请输入需要转账的金额:"))
                    (e["carid" == cardnum]) = (
                        e["carid"] == cardnum)-a_money  # 扣去转账用户的金额
                    (e["carid" == a_card]) = (
                        e["carid"] == a_card)+a_money  # 增加被转帐用户的金额
                    return
            else:
                print("银行卡输入错误！！！")
                return

    def CunPan(self):  # 存盘
        file = open("D:\python project\Bank\ljw.data", "w")
        file.write(str(user))
        file.close
        # 锁定

    def SuoDing(self):
        cardnum = input("请输入您的卡号：")
        for e in user:  # 遍历user用户列表
            if cardnum in e["carid"]:
                i = input("是否锁定账户！！输入Y/n")
                if i == "y" or i == "Y":
                    Data["onoff"] = "off"
                    print(f"账户已锁定{Data['onoff']}")
                    return
                else:
                    return
    # 解锁

    def JieSuo(self):
        cardnum = input("请输入您的卡号：")
        for e in user:  # 遍历user用户列表
            if cardnum in e["carid"]:
                i = input("是否解锁账户！！输入Y/n")
                if i == "y" or i == "Y":
                    Data["onoff"] = "on"
                    print(f"账户已解锁{Data['onoff']}")
                    return
                else:
                    return


a = Bank()
b = Printuser()

while True:
    b.atmview()
    try:
        i = input("请选择功能：")
    except TypeError:
        print("请输入数字选择！")
        break
    else:
        if i == "1":
            a.CreatUser()
        elif i == "2":
            a.SerchUser()
        elif i == "3":
            a.Cunkuan()
        elif i == "4":
            a.QuKan()
        elif i == "6":
            a.SuoDing()
        elif i == "8":
            a.JieSuo()
        elif i == "7":
            a.CunPan()
        elif i == "5":
            a.ZhuanZhang()
        elif i == "0":
            break
