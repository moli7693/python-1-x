# 定义实体类

# 订单小项类
class OrderItem(object):
    def __init__(self, itemid, productname, price, quantity=1):
        self.itemid = itemid      # 订单项编号
        self.productname = productname        # 商品名称
        self.price = price    # 商品单价
        self.quantity = quantity    # 该商品购买数量
    
    #########################################################################
    # 任务1相关：创建初始的订单和订单项对象
    #########################################################################
    # 定义只读的订单项总价属性
    #@____【1】____
    @property
    def totalprice(self):
        return self.price * self.quantity
    
    # 以指定的文本格式输出订单项的信息，以便print函数能直接输出该信息
    def __str__(self):
        return "订单项：{}, 名称：{}, 单价：{}, 数量：{}, 总价：{:.2f}".format(#____【3】____(
            self.itemid, self.productname, self.price, self.quantity, self.totalprice
        )


# 订单类
class Order:
    def __init__(self, orderid, orderdate):
        self.catid = orderid    # 订单编号
        self.orderdate = orderdate        # 订单日期
        self.items = []  # 该订单下所有订单项
    
    # 打印输出本订单所有订单小项信息
    def print_items(self):
        for item in self.items:
            print(item)
    
    # 将一个订单项添加到订单中
    def add_item(self, item):
        self.items.append(item)#____【4】____(item)

    # 计算订单总价(即：每个订单项的总价之和)
    def get_total(self):
        return sum([item.totalprice for item in self.items])#【6】])

    # 删除指定itemid的订单项
    def remove_item(self, itemid):
        target_item = None  # 记录待删除的订单项
        for item in self.items:
            # 找到了待删除的订单项
            if item.itemid == itemid:#____【7】____ itemid:
                target_item = item
                break
        # 从items中删除target_item
        if target_item:
            self.items.remove(target_item)#____【8】____(target_item)
    
    # 更新指定itemid的订单项的商品数量
    # 要求先检查quantity的值必须大于0，否则直接返回(不做任何操作)
    def update_item_quantity(self, itemid, quantity):
        if quantity <= 0:#____【9】____ 0:
          return    Exception("商品数量必须大于0")
            #____【10】____ Exception("商品数量必须大于0")
        # 找到指定的订单项，将其数量变更为传入的quantity参数值
        for item in self.items:
            if item.itemid == itemid:
                item.quantity = quantity
                break
