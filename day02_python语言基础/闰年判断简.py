r=int(input('输入年份：'))
if r % 4 == 0:
    if r %100 == 0:
        if r %400 ==0:
            print("{0}年闰年".format(r))
        else:print("{0}不是闰年".format(r))
    else:
        print("{0}是闰年".format(r))
else:
    print("{0}不是闰年".format(r))