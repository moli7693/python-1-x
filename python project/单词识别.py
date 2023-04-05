date ={'m':'Monday', 'tu':'Tuesday', 'w':'Wednesday', 'th':'Thursday', 'f':'Friday', 'sa':'Saturday', 'su':'Sunday'}
words = input('请输入字母：')
if words in date:
        print(date[words])				
elif words == 't' or words=='s':
        words_2 = input('请输入第二字母：')
        words_add = words + words_2			# 字符拼接
        if words_add in date:
            print(date[words_add])
        else:
            print("没有相关单词！后续会持续更新bwb")			# 打印键对应的值
else:
    print('没有相关单词!')
 