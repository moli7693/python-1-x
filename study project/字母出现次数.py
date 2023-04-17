str1='asjhsdjkgavsdjasdbj'
ds_str={}
for a_str1 in str1:
    if a_str1 in ds_str:
        ds_str[a_str1]+=1
    else:
        ds_str[a_str1]=1
#for c in ds_str.items():
   # print(c)
for i in ds_str.items():
    print(i)