#########################################################################
# 任务1：统计单个Python代码文件的有效代码行数
# 注意：
# (1)空行，或者只包含空格字符的行不计入
# (2)只包含注释语句的行不计入
#########################################################################
import os
print('【任务1开始】', '=' * 100)

# 定义计算代码文件有效行数的函数


def calc_code_lines(file_path):
    row_count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        # 一次性读完所有文本行
        for line in f.readlines():  # ____【1】____():
            # 去除该行开头和结尾的空格
            line = line.strip()  # ____【2】____()
            # # (1)如果该行长度为0，则不予计算
            if len(line) == 0:
                continue
            # # (2)如果该行以#字符开头，也不予计算
            if line.startswith('#'):  # ____【3】____('#'):
                continue
            row_count += 1
    return row_count


# 设置文件路径
filePath1 = 'D:\\python project\\test03\\file\\data1.txt'

print("文件非空行数：", calc_code_lines(filePath1))

print('【任务1结束】', '=' * 100)


#########################################################################
# 任务2：统计指定目录下所有.py文件的有效代码行数
#########################################################################
print('【任务2开始】', '=' * 100)


# 设置目录路径
dirPath = 'D:\\python project\\test03\\file'
total = 0

for item in os.listdir(dirPath):  # (____【4】____):
    # 如果不是以.py结尾，则跳过：
    if not item.endswith('.py'):
        continue
    # 合成完整路径
    full_path = os.path.join(dirPath, item)  # ____【5】____(dirPath, item)
    # 判断子项是否为文件
    if os.path.isfile(full_path):
        # ____【6】____(full_path):
        total += calc_code_lines(full_path)

print("所有.py文件代码总行数：", total)

print('【任务2结束】', '=' * 100)
