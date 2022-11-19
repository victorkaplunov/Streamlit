from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2],
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(
            selected_mode=True,
            orient="horizontal",
            pos_top="left",
            pos_right=10
        ),
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(
            is_show=False,
            feature=opts.ToolBoxFeatureOpts(
                brush=opts.ToolBoxFeatureBrushOpts(
                    rect_title="Прямоугольник",
                    polygon_title="Полигон",
                    line_x_title="Ось X",
                    line_y_title="Ось Y",
                    clear_title="Очистить заголовок",
                    keep_title="Сохранить заголовок"
                ),
                save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                    title="Сохранит как изображение"
                ),
                restore=opts.ToolBoxFeatureRestoreOpts(
                    title="Восстановить"
                ),
                data_view=opts.ToolBoxFeatureDataViewOpts(
                    title="Показать данные",
                    lang=["Данные графика", "Отказаться", "Сохранить"]
                ),
                data_zoom=opts.ToolBoxFeatureDataZoomOpts(
                    zoom_title="Увеличить",
                    back_title="Уменьшить"
                ),
                magic_type=opts.ToolBoxFeatureMagicTypeOpts(
                    line_title="Линейный",
                    bar_title="Столбчатый",
                    stack_title="Стопка",
                    tiled_title="Плитка"
                )
            )
        ),
    )
)
st_pyecharts(b)