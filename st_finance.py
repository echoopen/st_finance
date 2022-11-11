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
        styles = {'navtab': {'background-color':'#111',
                            'color': '#818181',
                            'font-size': '18px',
                            'transition': '.3s',
                            'white-space': 'nowrap',
                            'text-transform': 'uppercase'},
                'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                'cursor': 'pointer'}},
                'iconStyle':{'position':'fixed',
                            'left':'4.5px',
                            'text-align': 'left'},
                'tabStyle' : {'list-style-type': 'none',
                                'margin-bottom': '30px',
                                'padding-left': '5px'}},
        default_choice=0
        )

if tabs == '金融可视化':
    st.write('hello')