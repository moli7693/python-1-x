
# 定义变量
add = 0
s = 1
str_add = ''
inv_str_add = ''
# 带提示输入赋值
z = input('请输入需要加密的字符串：')
# 把字符串转换为ASCII码
for i in z:
    #nprint(i)
    add += ord(i)
    str_add += str(ord(i))
 
# 调试代码
#print(add)      # 打印转换ASCII码之和
#print(str_add)  # 打印转换ASCII码拼接
inv_str_add=str_add[::-1]
# 打印加密后的字符串
print ('加密后：',add+int(inv_str_add))
#print("加密后:",buf,add,int(inv_str_add))