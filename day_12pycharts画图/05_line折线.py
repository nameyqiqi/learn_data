import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
unit_price=['10','11','12','15','17','18']
num = [100,110,120,150,170,180]
c = (
    Line()
    .add_xaxis(unit_price)
    .add_yaxis("商家A",num)
    #.add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
    .render("line_base.html")
)