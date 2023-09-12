from pyecharts import options as opts
from pyecharts.charts import Map

# pyecharts的地图最多具体到市，区、县、村等没办法了。
# pyecharts要求提供的地图数据必须包含省、市字样。
data = [['宝山区', 300], ['崇明区', 200], ['普陀区', 150], ['浦东新区', 500], ['青浦区', 200], ['嘉定区', 50]]
print(data)
c = (
    Map()
    .add(series_name="", data_pair=data, maptype="上海")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-基本示例"),
        # 添加视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(min_=50, max_=500),
        toolbox_opts=opts.ToolboxOpts()

    )
    .render("map_base.html")
)