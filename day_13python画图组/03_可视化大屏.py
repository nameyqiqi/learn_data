# 规则：
# 一个大屏幕从左向右、从上向下按照问题的重点依次展示。
# 一个数据看板无法完全展示完，分多页，分多个看板展示。
# 第一个看版展示的不一定是问题，而是全年公司运营状况的总结。
# 例如：
# 连锁超市：先展示今年的销售额、总的成本、总的利润、总的门店数、新增门店数。
# 从第二页开始分类展示问题。
# 还可以利用：同比、环比与去年同期作比较。

from pyecharts.charts import Page, Map, Funnel
from pyecharts import options as opts

# pyecharts的地图最多具体到市，区、县、村等没办法了。
# pyecharts要求提供的地图数据必须包含省、市字样。
data = [['宝山区', 300], ['崇明区', 200], ['普陀区', 150], ['浦东新区', 500], ['青浦区', 200], ['嘉定区', 50]]
c = (
    Map()
    .add(series_name="", data_pair=data, maptype="上海")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-基本示例"),
        # 添加视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(min_=50, max_=500)
    )
)

data = [['展现量', 1000], ['点击量', 800], ['访问量', 400], ['咨询量', 100], ['订单量', 30]]
a = (
    Funnel()
    .add("商品", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
)


# 最终看板依据page添加的图表生成的
p = (
    # 声明Page顺序多图，同时说明布局使用Page提供的拖拽方式进行布局。
    Page(layout=Page.DraggablePageLayout)
    # 向page中添加图标
    .add(c, a)
    # 生成看板,上方add中添加的图表不使用其单独的render
    .render('./数据看板.html')
)