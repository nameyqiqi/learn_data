from pyecharts import options as opts
from pyecharts.charts import Bar

# 如果某些刻度标签（坐标轴标签）名字特别长，会影响到周围其他标签的显示，此时pyecharts做了自适应，自动隐藏掉几个标签。
x = ['哈士奇', '萨摩耶', '泰迪', '金毛', '牧羊犬牧羊犬牧羊犬牧羊犬牧羊犬', '吉娃娃', '柯基', '土狗', '阿拉斯加', '藏獒']
y1 = [141, 96, 112, 213, 70, 100, 129, 100, 60, 70]
y2 = [41, 51, 128, 123, 133, 137, 22, 200, 70, 80]
print(x, y1, y2)
c = (
    Bar()
    .add_xaxis(x)
    # stack:将柱子叠在一起，设置同样的名字
    .add_yaxis("商家A", y1,stack='one')
    .add_yaxis("商家B", y2,stack='one')
    # 柱状图转条形图:reversal_axis()
    .reversal_axis()
    # set_global_opts:全局配置项
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
        # 引入区域缩放配置项, is_show默认为True
        # 区域缩放配置项默认水平排列，当柱状图变为条形图，可能需要区域缩放跟着一起变
        # orient=horizontal(水平，默认)，vertical（垂直）
        datazoom_opts=opts.DataZoomOpts(orient='vertical'),
        # 引入坐标轴配置项, 如果是修改坐标轴，一定一定说明是哪个轴
        xaxis_opts=opts.AxisOpts(
            # 通过axislabel_opts参数，得知，再引入标签配置项
            # # 引入标签配置项修改坐标轴刻度的显示间隔，interval改为0，强制显示所有
            # rotate:标签旋转
            axislabel_opts=opts.LabelOpts(interval=0, rotate=-7)
        )
    )
    # set_series_opts:系列配置项
    # 如何指定到修改x轴刻度标签：坐标轴 > x坐标轴标签 > 标签
    # .set_series_opts(
    #     # 引入标签配置项修改坐标轴刻度的显示间隔，interval改为0，强制显示所有
    #     label_opts=opts.LabelOpts(interval=0)
    # )
    .render("bar_base.html")
)
