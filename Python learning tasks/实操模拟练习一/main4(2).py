#38.（共12.5分）
#任务要求：统计某个Python代码文件中有效代码行数。

#注意：空行或者只包含空格字符的行不计入有效行；只包含注释语句的行不计入有效行。

########代码开始######### 定义计算代码文件有效行数的函数
def calc_code_lines(file_path):
    row_count = 0
    #____【1】____ 
    with open(file_path, 'r', encoding='utf-8') as f:
        # 一次性读取所有文本行
         for line in f.readlines():#____【2】____():
        # 去除该行开头和结尾的空格
            line = line.strip()#____【3】____()
        #  (1)如果该行长度为0，则不予计算
            if len(line) == 0:#____【4】____(line) == 0:
                continue
        #  (2)如果该行以#字符开头，也不予计算
            if line.____【5】____('#'):
                continue
            row_count += 1
    return row_count

