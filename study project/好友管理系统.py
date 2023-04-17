list_f = []
print("""
欢迎使用好友管理系统
1.添加好友
2.删除好友
3.备注好友
4.展示好友
5.退出
""")
while True:
    n = int(input("请输入您的选项:"))
    if n == 1:
        f = input("请输入要添加的好友：")
        list_f.append(f)#为列表添加元素
        print("好友添加成功")
    elif n == 2:
        f = input("请输入删除好友姓名：")
        for b in list_f:
            if b==f:
                list_f.remove(f)#移除好友元素
                print("删除成功")
                continue
            else:
                print("无好友")
    elif n == 3:
        o_name = input("请输入要修改的好友姓名：")
        for a in list_f:
            if a==o_name:
                n_name = input("请输入修改后的好友姓名：")
                i = list_f.index(o_name)
                list_f[i] = n_name#修改元素
                print("备注成功")
                continue
            else:
                print("无好友")
    elif n == 4:
        if len(list_f) == 0:
            print("好友列表为空")
        else:
            for m in list_f:
                print(m)
    elif n == 5:
        break
print("关闭好友系统")
