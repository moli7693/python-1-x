#########################################################################
# 任务1：统计单个Python代码文件的有效代码行数
# 注意：
# (1)空行，或者只包含空格字符的行不计入
# (2)只包含注释语句的行不计入
#########################################################################
print('【任务1开始】', '=' * 100)

# 设置文件路径
filePath1 = 'file/data1.txt'

row_count = 0
with open(filePath1, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        # 去除该行开头和结尾的空格
        line = line.strip()
        # # (1)如果该行长度为0，则不予计算
        if len(line) == 0:
            continue
        # # (2)如果该行以#字符开头，也不予计算
        if line.startswith('#'):
            continue
        row_count += 1

print("文件非空行数：", row_count)

print('【任务1结束】', '=' * 100)



#########################################################################
# 任务2：将字典数据写入到csv文件中
#########################################################################
print('【任务2开始】', '=' * 100)

print('【任务2结束】', '=' * 100)