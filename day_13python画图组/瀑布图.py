from pyecharts.charts import Bar
from pyecharts import options as opts

x = ['一月', '二月', '三月', '四月', '五月']

y_1 = [0, 900, 800, 100, 100]
# 增加的
y_in = [900, 100, '-', '-', 200]
# 减少的
y_out = ['-', '-', 200, 700, '-']
# 1. 如果当前增加的基础上下一阶段增加，当前柱子的上边框与下一个柱子的下边框水平
# 2. 如果当前增加的基础上下一阶段是减少，当前柱子的上边框与下一个柱子的上边框水平。
# 3. 如果当前下降的基础上下一阶段是减少，当前柱子的下边框与下一个柱子的上边框水平。
# 4. 如果当前下降的基础上下一阶段是增加，当前柱子的下边框与下一个柱子的下边框水平。

# 5. 如果当前阶段是增加的，当前阶段的y_1 = 上个月剩的；当前阶段是减少，当前阶段的y_1是本阶段剩的。

A = (
    Bar()
    .add_xaxis(xaxis_data=x)
    # 修改最下方蓝色柱子，要把图元样式配置项写入到对应的add_yaxis中
    # rgb三元色可以拓展rgba --> a:表示透明度，从0~1，如果为0，透明
    .add_yaxis(
        series_name='', y_axis=y_1, stack='总量',
        itemstyle_opts=opts.ItemStyleOpts(color='rgba(0,0,0,0)')
    )

    .add_yaxis(series_name='', y_axis=y_in, stack='总量')
    .add_yaxis(series_name='', y_axis=y_out, stack='总量')
    .render('./瀑布图.html')
)