def get_sum(a,b):
    return a+b
m=get_sum(5,10)
print(m)

def get_stratum(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result
print(get_stratum(5))