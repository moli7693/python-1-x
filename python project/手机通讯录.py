print('=' * 20)
print("欢迎使用通讯录：")
print('1.添加联系人')
print('2.查看通讯录')
print('3.删除联系人')
print('4.修改联系人信息')
print('5.查找联系人')
print('6.退出')
print('=' * 20)
 
d = {}
 
 
while True:
 
    choic = input('请输入功能序号：')
 
    # 添加联系人
    if choic == '1':
        name1 = input('请输入联系人姓名：')
        num = input('请输入电话号码：')
        d[name1] = num
    
    # 查看通讯录
    elif choic == '2':
        # 判断字典d是否为空，下同
        if bool(d):
            for a in d.items():
                print(a)
        else:
            print('通讯录为空，请先添加联系人')
 
    # 删除联系人
    elif choic == '3':
        if bool(d):
            name3 = input('请输入要删除的联系人姓名：')
            d.pop(name3)
        else:
            print('通讯录为空，请先添加联系人')
 
    # 修改联系人信息
    elif choic == '4':
        if bool(d):
            print("8.修改联系人姓名 9.修改联系人电话号码")
            choic4 = input("请输入修改功能序号：")
            name4_1 = input('请输入原联系人姓名：')
            if choic4 == '8':
                while 1:
                    name4_2 = input('请输入修改后联系人姓名：')
                    if name4_2 in d:
                        print('联系人姓名已存在')
                    else:    
                        d[name4_2] = d[name4_1]
                        d.pop(name4_1)
                        break
            elif choic4 == '9':
                d[name4_1] = input('请输入修改后的电话号码：')
        else:
            print('通讯录为空，请先添加联系人')
 
    # 按联系人姓名查找联系人信息
    elif choic == '5':
        if bool(d):
            name5 = input("请输入要查找的联系人：")
            if name5 in d:
                print('联系人：{0}，电话号码：{1}'.format(name5,d[name5]))
            else:
                print('通讯录中没有该联系人')
        else:
            print('通讯录为空，请先添加联系人')
 
    # 退出
    elif choic == '6':
        print('bye~')
        break
    print('操作成功')
 
print('已退出应用')