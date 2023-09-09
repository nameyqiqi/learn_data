import pandas as pd
a=[1,2,3]
#非指定值
myvar=pd.Series(a)
print(myvar)
print(myvar[1])
#指定值
myvar=pd.Series(a,('x','y','z'))
print(myvar)

#构建Dataframe
data = [['Google',10],['Runoob',12],['Wiki',13]]
print(a)
frame=pd.DataFrame(data)
print(frame)
#打印0行 1行
print(frame.loc[[0,1]])     
#通过索引搜索
print(frame[1],'---')