# 定义实体类

# 商品类
class Product(object):
    def __init__(self, prodid, name, listprice, discount, catetory):
        self.empid = prodid      # 商品编号
        self.name = name        # 商品名称
        self.listprice = listprice    # 商品标价
        self.discount = discount    # 商品折扣
        self.cat = catetory        # 商品所属的类别对象
    
    #########################################################################
    # 任务1相关：创建初始的类别和商品对象
    #########################################################################
    # 定义只读的实际价格属性
    # 商品标价诚意商品折扣
    #@____【1】____
    @property
    def actualprice(self):
        return self.listprice * self.discount
    
    # 以指定的文本格式输出商品的信息
    def __str__(self):
        # 获取所属类别名称(如果没有所属类别，则返回'无类别')
        cat_name = self.cat.name if self.cat else '无类别'#____【2】____ self.cat ____【3】____ '无类别'
        return "%s, %s, %.2f, %s" % (self.name, self.discount, self.listprice, cat_name)


# 商品类别类
class Category:
    def __init__(self, catid, name):
        self.catid = catid    # 类别编号
        self.name = name        # 类别名称
        self.products = set()  # 类别下所有商品对象
    
    # 打印输出本类别所有商品信息
    def print_products(self):
        for product in self.products:
            print(product)