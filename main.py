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
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.write(dict_, unsafe_allow_html=True)