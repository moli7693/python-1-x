from entity import Product, Category


#########################################################################
# 任务1：创建初始的类别和商品对象
# 本任务需要补全Product类的acturalprice属性和__str__函数代码
#########################################################################
print('【任务1开始】', '=' * 100)

cat1 = Category(1, '笔记本电脑')

prod1 = Product(1001, '联想ThinkPad E14 2021', 6000.0, 0.99, cat1)
prod2 = Product(1002, 'RedmiBook Pro 14增强版', 5500.0, 0.95, cat1)
prod3 = Product(1003, '荣耀笔记本电脑MagicBook X14', 4000.0,  0.97, cat1)
prod4 = Product(1004, '华为笔记本电脑MateBook 14', 6500,  0.96, cat1)

# 输出prod1的信息
print("prod1的信息：", prod1)
print("prod1的实际价格：", prod1.actualprice)

print('【任务1结束】', '=' * 100)



#########################################################################
# 任务2：将商品与类别关联
#########################################################################
print('【任务2开始】', '=' * 100)

# 将所有商品加入cat1
for prod in [prod1, prod2, prod3, prod4]:
    cat1.products.add(prod)#____【4】____)

# 输出cat1类别所有商品信息
print("cat1下所有商品信息：")
cat1.print_products#____【5】____()

print('【任务2结束】', '=' * 100)



#########################################################################
# 任务3：根据条件查找匹配的商品信息
#########################################################################
print('【任务3开始】', '=' * 100)

# 在cat1类别内查找所有listprice低于6000的商品
listprice = 6000.0
results = filter(lambda prod: prod.listprice< listprice, cat1.products)
                 #____【6】____ < listprice, cat1.products)
# 查询结果转换成list
results_list = list(results)#____【7】____(results)
print("listprice低于6000的商品:")
for result in results_list:
    print(result)

# 在cat1类别内查找姓名包含字符'14'的商品
keyword = '14'
# 姓名匹配并构造匹配的对象
results = [Product for Product in cat1.products if keyword in Product.name]
           # ____【8】____ Product.name]
print("cat1下姓名包含", keyword, "的商品：")
for result in results:
    print(result)

print('【任务3结束】', '=' * 100)



#########################################################################
# 任务4：根据实际价格进行排序
#########################################################################
print('【任务4开始】', '=' * 100)

# 定义按actualprice进行比较的函数
def compare_by_actualprice(prod):
    return prod.actualprice

# 将cat1的商品集合转换成list
Products = list(cat1.products)
# 根据actualprice从高到底排序
Products.sort(key=compare_by_actualprice,reverse= True)#____【9】____, reverse=____【10】____)
for prod in Products:
    print(prod)

print('【任务4结束】', '=' * 100)