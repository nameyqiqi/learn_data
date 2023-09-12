#包，又被叫做模块，库
#包python自带的，还有需要安装的
#包如何安装： 使用pip命令

#二. 安装
#1. 借助pycharm的可视化安装
#2. 使用pip命令安装

# 可视化安装
# Windows： file-setting-project-python interpreter
# mac：pip3 模块名

#from pypinyin import pinyin
#for i in range(int('4e00',16),int('8fa5',16)):
#    print(chr(i),pinyin(chr(i),heteronym=True),end='')

#有进度条不能有print
from tqdm import tqdm
import time
for i in tqdm(range(100000),desc='这是一个进度条'):
    pass
    #time.sleep(0.1)
    #print(i)


