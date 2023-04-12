#完成后的OrderItem类，在通过下列方式进行调用时： 

#输出的结果应该为：订单项：1001, 名称：RedmiBook Pro 14增强版, 单价：5500.0, 数量：2, 总价：11000.00 
  
########代码开始######## 
class OrderItem:
    # 构造函数
    def __init__(self, itemid, productname, price, quantity=1):
    #____【1】____(self, itemid, productname, price, quantity=1):
        self.itemid = itemid      # 订单项编号
        self.productname = productname        # 商品名称
        self.price = price    # 商品单价
        self.quantity = quantity    # 该商品购买数量
    # 定义只读的订单项总价属性
    #@____【2】____
    @property
    def totalprice(self):                                                                                                                                                                                                                                                                          
        return self.price * self.quantity
  
    # 以指定的文本格式输出订单项的信息，以便print函数能直接输出该信息
    def __str__(self):#____【3】____):
        return "订单项：{}, 名称：{}, 单价：{}, 数量：{}, 总价：{: .2f}".format(#____【4】____(
            self.itemid, self.productname, self.price, self.quantity, self.totalprice#____【5】____
        ) 
########代码结束########
item = OrderItem(1001, 'RedmiBook Pro 14增强版', 5500.0, 2) 
print(item)