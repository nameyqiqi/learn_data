str='Python2023'
re_str=''
a = input("please give number:")
if 0<int(a)<10:
    re_str=str+'00'+a
if 10<int(a)<100:
    re_str=str+'0'+a
if 100<int(a)<1000:
    re_str=str+a
print(re_str)