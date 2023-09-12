import ddddocr
#读取图片
with open('./image/1.png','rb') as f:
    data=f.read()
# 创建ddddocr对象
ocr1 = ddddocr.DdddOcr()
code=ocr1.classification(data)
print(code)
