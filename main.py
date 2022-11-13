import streamlit as st

st.set_page_config(
   page_title="Streamlit test app",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title('Streamlit test app')

dict_ = "<h1>HTML repr</h1>"
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")

   from pyecharts import options as opts
   from pyecharts.charts import Bar
   from streamlit_echarts import st_pyecharts

   b = (
      Bar()
      .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
      .add_yaxis(
         "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
      )
      .set_global_opts(
         title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
         ),
         toolbox_opts=opts.ToolboxOpts(
            feature=opts.ToolBoxFeatureOpts(
               brush=opts.ToolBoxFeatureBrushOpts(
                  rect_title='Прямоугольник',
                  polygon_title='Полигон',
                  line_x_title='Ось X',
                  line_y_title='Ось Y',
                  clear_title='Очистить заголовок',
                  keep_title='Сохранить заголовок'
               ),
               save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                  title='Сохранит как изображение'
                  ),
               restore=opts.ToolBoxFeatureRestoreOpts(
                  title='Восстановить'
                  ),
               data_view=opts.ToolBoxFeatureDataViewOpts(
                  title='Показать данные',
                  lang=["Данные графика", "Отказаться", "Сохранить"]
                  ),
               data_zoom=opts.ToolBoxFeatureDataZoomOpts(
                  zoom_title='Увеличить',
                  back_title='Уменьшить'
                  ),
               magic_type=opts.ToolBoxFeatureMagicTypeOpts(
                  line_title='Линейный',
                  bar_title='Столбчатый',
                  stack_title='Стопка',
                  tiled_title='Плитка'


               )

            )
         ),
      )
   )
   st_pyecharts(b)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# To create the sidebar
st.sidebar.write("My Sidebar")

# To add elements in the sidebar
st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write(dict_, unsafe_allow_html=True)