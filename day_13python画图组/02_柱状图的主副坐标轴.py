from pyecharts.charts import Bar
from pyecharts import options as opts
data_1 = ['100','200','300','400']
data_2 = ['20','50','80','150']
a = (
    Bar()
    .add_xaxis(['一月','二月','三月','四月'])
    .add_yaxis(series_name="降雨量",y_axis=data_1,yaxis_index=1)
    .add_yaxis(series_name="蒸发量",y_axis=data_2,yaxis_index=0)
    #.reversal_axis()
    # 负轴指向1
    .extend_axis(
        yaxis=opts.AxisOpts(
            name='降雨量',
            min_=0,
            max_=500
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name='蒸发量',
            min_=0,
            max_=150,

        )

    )
    .render('./tu/bar_double.html')

)