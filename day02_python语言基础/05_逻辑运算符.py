# and（逻辑与运算）、or（逻辑或运算）、not（逻辑非运算）
# 备注：逻辑运算结果也是布尔类型的结果

# and： 条件1 and 条件2，只有两个条件都成立，整体条件才成立。
# 中断机制：只要and左边条件不成立，直接得结果False。
BMI = 23
print(BMI >= 18.5 and BMI <= 23.9)

# or：条件1 or 条件2，只有两个条件都不成立，整体才不成立。
# 中断机制：只要or左边成立，直接得结果True。
# 判断BMI是否为非正常
BMI = 25
print(BMI <= 18.5 or BMI >= 23.9)

# 练习：判断一个年份是否是闰年
# 条件1：年份能被4整除但是不能被100整除。2004
# 条件2：年份能被400整除。 2000
year = 2001
result = (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0)
print(result)

result_1 = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(result_1)

print('************ not知识点 ************')
# not：直接将结果取反
# not 条件
print(not True)




