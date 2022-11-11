import streamlit as st
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    layout='wide',
)

st.markdown('<style>' + open('./css/style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(
        tabName=['金融可视化'],
        iconName=['dashboard'],
        default_choice=0
        )

if tabs == '金融可视化':
    st.write('hello')