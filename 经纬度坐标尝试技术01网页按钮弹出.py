import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# 设置页面标题
st.title("地图查看器")

# 初始化会话状态，用于控制地图显示
if 'show_map' not in st.session_state:
    st.session_state.show_map = False

# 显示按钮，控制地图显示状态
if st.button("显示地图"):
    st.session_state.show_map = not st.session_state.show_map

# 当需要显示地图时
if st.session_state.show_map:
    # 创建地图实例
    m = folium.Map(
        location=[39.917834, 116.397036],  # 北京位置
        zoom_start=13, 
        width='100%',
        height='600px', 
        zoom_control=False,
        tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}&ltype=6',
        attr='AutoNavi'
    )
    
    # 添加点击显示经纬度的功能
    m.add_child(folium.LatLngPopup())
    
    # 在Streamlit中显示地图
    map_data = st_folium(m, width=700, height=500)
    
    # 检查是否有点击数据并处理
    if map_data.get('last_clicked'):
        lat = map_data['last_clicked']['lat']
        lng = map_data['last_clicked']['lng']
        st.success(f"点击位置经纬度: 纬度 {lat:.6f}, 经度 {lng:.6f}")
        # 在控制台打印经纬度
        print(f"用户点击位置 - 纬度: {lat:.6f}, 经度: {lng:.6f}")