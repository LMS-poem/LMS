import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


add_selectbox=st.sidebar.selectbox(
    'please choose a checklink',
    ('烟花.jpg','烟花.mp4')
)
if add_selectbox=='烟花.jpg':
    st.title('动漫:blue[烟花]海报')
    st.caption('app_this :red[李明森 made]')
    #img1=Image.open('D:\\Downloads\\yanhua.jpg')
    st.image('https://cdn.pixabay.com/photo/2016/11/14/03/21/fireworks-1822479_1280.jpg')
    st.header('真想:blue[回到那个夏天,愿今夜永不结束]')
    st.snow()
elif add_selectbox=='烟花.mp4':
    st.title('全球:blue[烟花]盛宴')
    st.caption('app_this :red[李明森 made]')
    #vidio_filed=open('D:\\Downloads\\打上花火.mp4','rb')
    #vidio_bytes=vidio_filed.read()
    st.video('https://mazwai.com/videvo_files/video/free/2015-05/small_watermarked/scarabee-images--rushs_lumix_gh4_in_4k_fireworks_paris_preview.webm',format='video/mp4')
    st.balloons()
text=st.text_input('看看:blue[烟花]吧','refuse 精神内耗')
st.write('the text you input is',text)

