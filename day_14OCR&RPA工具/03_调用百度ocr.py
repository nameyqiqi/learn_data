#从百度aip模块引入ocr识别的包
from aip import AipOcr

AppId ='37823474'
Apikey = 'NkSMRd19wHyeXvjuCFFMbF8Y'
Secretkey = 'bZHh8QALowt4IAxVgkNztpsUREI6aTuS'
#验证服务
server_result = AipOcr(AppId,Apikey,Secretkey)
print(server_result)

f = open('./image/3.jpg','rb')
image_data=f.read()
f.close()
# 调用服务识别
result=server_result.basicGeneral(image=image_data)
print(result)
