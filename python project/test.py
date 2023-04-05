class IdCardExceptin(Exception):  # 自定义身份证异常
    def __init__(self, length):
        self.length = length


try:
    idCard = input("请输入您的身份证号：")
    if len(idCard) != 18:
        raise IdCardExceptin(len(idCard))
except IdCardExceptin as result:
    print(f"身份证错误！！！！,你输入的长度为{result.length}身份证号码应当18位")
# 用户登录（三次机会）
flag = 0
for i in range(3):
    name = input()
    paw = input()
    if name == 'Kate' and paw == '666666':
        flag = 1
        print("登录成功！")
        break
if flag == 0:
    print("3次用户名或者密码均有误！退出程序。")
