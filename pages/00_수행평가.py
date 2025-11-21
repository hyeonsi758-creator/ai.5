# -*- coding: utf-8 -*-
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

def main():
    st.set_page_config(page_title="한국인이 좋아하는 해외 관광지 Top10", layout="wide")
    st.title("한국인이 좋아하는 해외 관광지 Top10 — 지도")
    st.write("사이드바에서 표시 개수와 클러스터 사용 여부를 선택하세요.")

    # 데이터 (간단하고 ASCII/UTF-8 호환)
    places = [
        {"rank": 1, "name": "Shibuya Crossing (Tokyo, Japan)", "lat": 35.6595, "lon": 139.7005, "info": "도쿄의 대표 장소"},
        {"rank": 2, "name": "Dotonbori (Osaka, Japan)", "lat": 34.6687, "lon": 135.5013, "info": "오사카의 유명 번화가"},
        {"rank": 3, "name": "Taipei 101 (Taipei, Taiwan)", "lat": 25.033968, "lon": 121.564468, "info": "타이베이 랜드마크"},
        {"rank": 4, "name": "Grand Palace (Bangkok, Thailand)", "lat": 13.75, "lon": 100.4913, "info": "방콕의 왕궁"},
        {"rank": 5, "name": "Victoria Peak (Hong Kong)", "lat": 22.275, "lon": 114.1455, "info": "홍콩 전망대"},
        {"rank": 6, "name": "Marina Bay Sands (Singapore)", "lat": 1.2834, "lon": 103.8607, "info": "싱가포르 명소"},
        {"rank": 7, "name": "Kuta Beach (Bali, Indonesia)", "lat": -8.7179, "lon": 115.1681, "info": "발리의 인기 해변"},
        {"rank": 8, "name": "Eiffel Tower (Paris, France)", "lat": 48.8584, "lon": 2.2945, "info": "파리의 상징"},
        {"rank": 9, "name": "Tower Bridge (London, UK)", "lat": 51.5055, "lon": -0.0754, "info": "런던의 명소"},
        {"rank":10, "name": "Ha Long Bay (Vietnam)", "lat": 20.9101, "lon": 107.1839, "info": "베트남 자연유산"},
    ]

    # 사이드바 옵션
    st.sidebar.header("옵션")
    n_show = st.sidebar.slider("표시할 관광지 수", min_value=1, max_value=10, value=10)
    use_cluster = st.sidebar.checkbox("마커 클러스터 사용", value=True)

    # Folium 지도 생성
    m = folium.Map(location=[20, 0], zoom_start=2)

    if use_cluster:
        cluster = MarkerCluster()
        m.add_child(cluster)

    for p in places[:n_show]:
        popup = f"<b>{p['rank']}. {p['name']}</b><br>{p['info']}"
        color = "red" if p["rank"] == 1 else "blue"
        marker = folium.Marker(
            location=[p["lat"], p["lon"]],
            popup=popup,
            tooltip=f"{p['rank']}. {p['name']}",
            icon=folium.Icon(color=color, icon="info-sign")
        )
        if use_cluster:
            marker.add_to(cluster)
        else:
            marker.add_to(m)

    st.subheader("지도")
    st.write("마커를 클릭하면 팝업이 열립니다.")
    st_data = st_folium(m, width=1100, height=700)

    if st_data and "last_object_clicked" in st_data:
        st.sidebar.write("### 클릭 정보")
        st.sidebar.json(st_data["last_object_clicked"])

if __name__ == "__main__":
    main()
