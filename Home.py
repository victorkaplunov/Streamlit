import streamlit as st

st.set_page_config(
   page_title="Streamlit test app",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
   menu_items={'Get help': None,
               'About': 'Some description',
               'Report a Bug': None}
)

st.title("Streamlit test app")


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")



   from streamlit_echarts import st_echarts

   options = {
      "legend": {
         # // Try "horizontal"
         "orient": "horizontal",
         # "right": 10,
         "top": "bottom"
      },
      "dataset": {
         "source": [
            ["product", "2015", "2016", "2017"],
            ["Matcha Latte", 43.3, 85.8, 93.7],
            ["Milk Tea", 83.1, 73.4, 55.1],
            ["Cheese Cocoa", 86.4, 65.2, 82.5],
            ["Walnut Brownie", 72.4, 53.9, 39.1]
         ]
      },
      "xAxis": {"type": "category"},
      "yAxis": {},
      "series": [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}]
   }
   print(options)
   st_echarts(options=options)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# To create the sidebar
st.sidebar.write("My Sidebar")



# st.write(comment, unsafe_allow_html=True)