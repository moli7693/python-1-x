d=input("请输入地区编号（华东地区01，华南地区02，华北地区03）：")
if d=='01':
    height=float(input('请输入快递重量（kg）:'))
    if height<=2:
        print("该收取费用：",height*13)
    else:
        print("该收取费用：",height*13+(height-2)*3,'元')

elif d=='02':
    height=float(input('请输入快递重量（kg）:'))
    if height<=3:
        print("该收取费用：",height*12)
    else:
        print("该收取费用：",height*12+(height-2)*2,'元')

elif d=='03':
    height=float(input('请输入快递重量（kg）:'))
    if height<=3:
        print("该收取费用：",height*14)
    else:
        print("该收取费用：",height*14+(height-2)*4,'元')
