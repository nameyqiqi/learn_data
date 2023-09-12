import  easyocr

# 1. 初始化模型
# lang_list : 将需要识别的语言代号存放在列表中
reader=easyocr.Reader(
    lang_list=['en','ch_sim'], #需要读取
    gpu=False, #不使用gpu
    download_enabled=False,#下载对应语言合集包,
    model_storage_directory='./model'
)
# 读取图片
# image可以接收两种形式：1.图片路径及名称，2.图片的二进制数据
result=reader.readtext(image='./image/2.png')
print(result)