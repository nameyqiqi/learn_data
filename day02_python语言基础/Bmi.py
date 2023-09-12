sg=float(input("请输入身高（cm）："))

tz=float(input("请输入体重（kg）："))

bmi = tz/((sg/100) ** 2)
if(bmi<18.5):
    print('偏瘦,BMI:',bmi)
elif 18.5<=bmi<=23.9:
    print('正常,BMI:',bmi)
elif 23.9<=bmi<27:
    print('偏重,BMI:',bmi)
elif 27<=bmi<=28:
    print('肥胖,BMI:',bmi)
else:
    print('重度肥胖,BMI:',bmi)



