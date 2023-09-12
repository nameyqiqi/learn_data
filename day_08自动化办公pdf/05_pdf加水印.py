#再导入一个具有实质性转换的方法 Transformation()
from  pypdf import PdfWriter,PdfReader,Transformation
# 1.读取需要添加水印的文件
r_1 = PdfReader('./pdf合集/1.pdf')
# 2.读取水印文件
r_2 = PdfReader('./pdf合集/water.pdf')
# 3.给r_1对应每一页都添加水印
# water.pdf只有一页内容（水印），盖到其他页面上方
# 4.for循环以前实现pdf创建
w_1=PdfWriter()

for i in range(0,len(r_1.pages)):
    page=r_1.pages[i]
    #merge_transformed_page() merge:合并 transformed转换
    # 将r_1的每一页与r_2的第一页合并，转换
    # transformed:把pdf转换为三维（告知如何合并的）
    page.merge_transformed_page(r_2.pages[0],Transformation())
    w_1.add_page(page)
# 5.保存
with open('./pdf合集/1sy.pdf','wb')as f:
    w_1.write(f)
