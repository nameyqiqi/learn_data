# 元数据：Metadata
# 元数据：这个pdf的各种信息（创建时间、作者、版本等）

from pypdf import PdfReader

# 1. 读pdf
r_1 = PdfReader('./pdf合集/3.pdf')
# 2. 读取pdf中的元数据
print(r_1.metadata)
# creator:创作者  --> Chromium :谷歌浏览器内核
# producer：生产者 --> Skia/PDF m80:谷歌内部PDF项目
# CreationDate：创建时间，基于此网站所在服务器的时间
# ModDate：同CreationDate

# 二、自己编写元数据，赋予pdf
# 再导入PdfWriter：pdf写操作
from pypdf import PdfWriter

# 1. 只要是对PDF进行修改，不允许从原文件修改，必须新建新的pdf
# PdfWriter()在新建新的空白的pdf
w_1 = PdfWriter()
# 2. 将原本的PDF完完整整的先copy一份
# 读出来的pdf.pages --> 相当于将每一页存放在容器中
for i in r_1.pages:
    # add_page向空白pdf中添加新页面
    w_1.add_page(i)

# 3. 将原本的pdf的元数据再加进来
w_1.add_metadata(r_1.metadata)

# 4. 编写自己的metadata，写入到w_1
# 字典：一一对应
# /Author --> 这个写法遵循谷歌的规范
data = {'/Author': 'olaf', '/Edu': '清华'}
w_1.add_metadata(data)

# 5. 将新的修改过的PDF保存
# open:打开， wb：writebytes  --> 使用二进制数据写（计算机中所有文件均已二进制形式存在）
# open结合wb，会判断指定路径下的文件是否存在，如果没有，自动创建，
# as：给创建或打开的这个文件起名字（变量）
# with：会自动关掉文件
with open('./pdf合集/new_pdf.pdf', 'wb') as f:
    # 将w_1这个变量对应的pdf数据写入到文件中即可
    w_1.write(f)  # w_1