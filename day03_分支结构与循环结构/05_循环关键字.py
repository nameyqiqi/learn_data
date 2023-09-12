#break: 使用在循环内部，只要有break被执行，立刻结束当前所在循环

#1.使用while计算1-100的和
i = 1
total = 0
while True:
    total += i
    if i == 100:
        break
    i += 1
print(i)
