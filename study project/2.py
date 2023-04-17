# ATM类
import random


class ATM(object):
    def __init__(self, allusers, Data):
        # 存储所有用户的信息，用字典
        self.allUsers = allusers
        self.Data = Data

    # 服务界面
    def atmview(self):
        print("**********************************************")
        print("*           开户（1）     查询（2）             *")
        print("*           存款（3）     取款（4）             *")
        print("*                   退出（0）                 *")
        print("**********************************************")

    # 开户
    def CreatUser(self):
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号：")
        phone = input("请输入您的电话号码：")
        Passwd = input("请输入密码：")
        cardid = str(random.randint(100000, 999999))  # 随机生成六位数卡号
        preMoney = int(input("请输入您的预存款金额："))
        if preMoney < 0:
            print("预存款输入有误，开户失败......")
            return -1
        # card = Card(cardid, Passwd, preMoney)
        # user = User(name, idCard, phone, card)
        self.Data["Passwd"] = Passwd
        self.Data["preMoney"] = preMoney
        self.Data["name"] = name
        self.Data["idCard"] = idCard
        self.Data["phone"] = phone
        self.allUsers[cardid] = self.Data
        print("开户成功，请牢记卡号:(%s)" % cardid)

    # 查询
    def SerchUser(self):
        cardnum = input("请输入您的卡号：")
        user = self.allUsers.get(cardnum)
        if user:
            cardpass = input("请输入您的密码：")
            if self.allUsers[cardnum]["Passwd"] != cardpass:
                print("密码输入错误")
                return -1
        else:
            print("卡号输入错误")
            return -1
        print("账号：%s    余额：%s" % (cardnum, self.allUsers[cardnum]["preMoney"]))

    # 取款
    def AddMony(self):
        cardnum = input("请输入您的卡号：")
        user = self.allUsers.get(cardnum)
        if user:
            cardpass = input("请输入您的密码：")
            if self.allUsers[cardnum]["Passwd"] != cardpass:
                print("密码输入错误")
                return -1
        else:
            print("卡号输入错误")
            return -1
        addmony = int(input("请输入存款金额："))
        self.allUsers[cardnum]["preMoney"] = self.allUsers[cardnum]["preMoney"] + addmony
        print("账号：%s    余额：%s" % (cardnum, self.allUsers[cardnum]["preMoney"]))

    # 取款
    def GetMony(self):
        cardnum = input("请输入您的卡号：")
        user = self.allUsers.get(cardnum)
        if user:
            cardpass = input("请输入您的密码：")
            if self.allUsers[cardnum]["Passwd"] != cardpass:
                print("密码输入错误")
                return -1
        else:
            print("卡号输入错误")
            return -1
        getmony = int(input("请输入取款金额:"))
        if user.card.cardMoney < getmony:
            print("余额不足，取款失败")
        self.allUsers[cardnum]["preMoney"] = self.allUsers[cardnum]["preMoney"] - getmony
        print("账号：%s    余额：%s" % (cardnum, self.allUsers[cardnum]["preMoney"]))


a = ATM()
a.CreatUser()
