# pyecharts中的charts存放了可以画的图，导入饼图
from pyecharts.charts import Pie
# faker是pyecharts提供的数据集（随机的），导入数据集Faker
from pyecharts.faker import Faker
# 导入配置项包
from pyecharts import options as opts
# 导入主题库
from pyecharts.globals import ThemeType

data = [list(z) for z in zip(Faker.choose(), Faker.values())]
print(data)
# 链式调用
A = (
    # 声明饼图：初始化是在声明图形时就规定好的
    Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    # 向饼图添加数据
    # 系列名称(series_name)属于大分类、这个图的数据对应的内容是小分类,系列名称如果没有设为空字符串
    # 第二个参数为图表需要的数据，饼图：[[名称(小分类), 数值],[名称(小分类), 数值],[名称(小分类), 数值]]
    # radius:饼图的内外半径（设置环形图的关键）
    .add(series_name="", data_pair=data, radius=['50%', '70%'])
    # 引入全局配置项
    .set_global_opts(
        # 从全局配置项中引入标题配置项,
        # 配置项等号左边怎么写：配置项名字字母全小写，opts前加下划线
        # title:主标题内容    pos_left:标题距离容器左侧的距离（position）
        title_opts=opts.TitleOpts(title='饼图案例', pos_left='center'),
        # 添加图例配置项: orient：改图例的水平或垂直布局，pos_top/left修改图例距离上方/左侧的距离
        legend_opts=opts.LegendOpts(is_show=True, pos_top='7%', pos_left='right', orient='vertical'),
        # 添加提示框配置项：通过formatter修改提示框内容样式，画饼图时，formatter有一个{d}表示占比
        # {b}:数据名, {c}:数值， {d}占比
        tooltip_opts=opts.TooltipOpts(formatter='{b}：{c}（{d}%）')
    )
    # 生成图表
    .render("./图表/pie_base.html")
)