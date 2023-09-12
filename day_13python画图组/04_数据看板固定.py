from pyecharts.charts import Page

Page.save_resize_html(
    source='./tu/total.html',
    cfg_file='./tu/chart_config.json',
    dest='./数据看板finall.html.'

)