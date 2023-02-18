import requests as req
import bs4
from time import sleep
import random
import re
import streamlit as st
st.set_page_config(page_title='LMS经管知识查询网站', 
                   page_icon='https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_1280.jpg',
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items=None
                  )
st.title(':red[经管]:blue[知识查询]:dollar:')
st.caption(':green[LMS]:cn:')
st.image('https://ts1.cn.mm.bing.net/th/id/R-C.435554e127a73a9218292dbfd1589aa9?rik=dlzAETciLSr8Lg&riu=http%3a%2f%2fwww.yueshi-edu.com%2fuploads%2fallimg%2f2006%2f201910171571321098222814.jpg&ehk=DviJFepPXEk%2bOxMnHqk3GBQd5PvyWtvjC7s661EKjUM%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1')
st.subheader(':red[出现乱码不要怕,我也没法解决它]:dog:')
st.audio('https://home.aigei.com:8443/0-r8/GeiFileLocalStore/b63/src/aud/mp3/bd/bdceab125a23446fa432ecd1a77d4d6b.mp3?download/%E7%BA%A6%E7%BF%B0%E5%B8%95%E5%88%87%E8%B4%9D%E5%B0%94+-+%E6%9D%9C%E5%B0%94%E7%9A%84%E5%8D%A1%E5%86%9C_%E7%88%B1%E7%BB%99%E7%BD%91_aigei_com.mp3&e=1676762340&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:mlFWcSTD3PLO-nMq7KGmw6duva0=')
keyword=st.text_area(':blue[请输入您想搜索的经管知识,也支持查找大学等其他内容]:red[不要打回车,LMS会做梦]:point_down:','''辽宁工程技术大学''')
st.snow()
if st.button('搜索来敲醒LMS'):
    url='https://wiki.mbalib.com/wiki/'+keyword
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
    }
    r=req.get(url,headers=header)
    r.encoding='utf-8'
    sleep(random.uniform(1,2))
    data=r.text
    html=bs4.BeautifulSoup(data)
    bd=html.select('#bodyContent > p')
    for i in bd:
        p=str(i)
        i2=re.sub(r'[<>qwertyuioplkjhgfdsazxcvbnm%@=\/-]','',p)
        st.write(i2)
    st.balloons()
else:
    st.write(':blue[LMS在睡觉，搜索叫醒他]:sleeping:')
    
    
