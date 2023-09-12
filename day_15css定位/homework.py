#判断水仙花数 153=1**3+5**3+3**3 while for循环
# for i in range(100,1000):
#     gw = i % 10
#     sw = i // 10 % 10
#     bw = i //100
#     if gw**3+bw**3+sw**3==i:
#         print(i)
# i = 100
# while i < 1000:
#     gw = i % 10
#     sw = i // 10 % 10
#     bw = i // 100
#     if gw**3+bw**3+sw**3==i:
#         print(i)
#     i+=1

#封装函数实现成绩是否及格
def score_result(s):
    if s<60:
        return False
    else:
        return True
print(score_result(55))

