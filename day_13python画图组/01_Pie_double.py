from pyecharts.charts import Pie
from pyecharts import options as opts
data_1 = [['青少年',100],['青年',200]]
data_2 = [['people',300],['old',100]]
a = (
    Pie(init_opts=opts.InitOpts(width='1000px',height='500px'))
    .add("我没k",data_1,center=['30%','50%'])
    .add("我没k",data_2,center=['75%','50%'])
    .render('./tu/饼图堆.html')
)