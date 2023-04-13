from entity import OrderItem, Order

#########################################################################
# 测试1：创建初始的订单和订单项对象
#########################################################################
print('【测试1开始】', '=' * 100)

order1 = Order(1, '2021-10-03 15:30:00')

item1 = OrderItem(1001, '联想ThinkPad E14 2021', 6000.0)
item2 = OrderItem(1002, 'RedmiBook Pro 14增强版', 5500.0, 2)
item3 = OrderItem(1003, '荣耀笔记本电脑MagicBook X14', 4000.0, 1)
item4 = OrderItem(1004, '华为笔记本电脑MateBook 14', 6500, 3)

# 将所有商品加入dept1
for item in [item1, item2, item3, item4]:
    order1.add_item(item)

# 输出order1类别所有商品信息
print("order1下所有商品信息：")
order1.print_items()

print('【测试1结束】', '=' * 100)


#########################################################################
# 测试2：计算订单总价
#########################################################################
print('【测试2开始】', '=' * 100)

print("order1下的订单总价:", order1.get_total())

print('【测试2结束】', '=' * 100)



#########################################################################
# 测试3：更新订单数量
#########################################################################
print('【测试3开始】', '=' * 100)

try:
    order1.update_item_quantity(item1.itemid, 2)
    order1.update_item_quantity(item2.itemid, -1)
except Exception as ex:
    print(ex)

order1.print_items()

print('【测试3结束】', '=' * 100)



#########################################################################
# 测试4：删除订单项
#########################################################################
print('【测试4开始】', '=' * 100)

order1.remove_item(item1.itemid)
order1.print_items()

print('【测试4结束】', '=' * 100)