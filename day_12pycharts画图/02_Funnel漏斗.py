from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker
li = [list(z) for z in zip(Faker.choose(), Faker.values())]
print(li)
c = (
    Funnel()
    .add("商品",li )
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
    .render("funnel_base.html")
)
