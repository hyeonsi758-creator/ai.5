import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Seoul Top10 - For Foreigners", layout="wide")

st.title("서울 — 외국인에게 인기있는 관광지 Top 10 🌏🇰🇷")
st.markdown("서울에서 외국인 관광객에게 인기있는 주요 명소 10곳을 Folium 지도로 표시합니다.")

# Top10 장소 데이터 (이름, 위도, 경도, 간단 설명)
PLACES = [
    {"name": "Gyeongbokgung Palace (경복궁)", "lat": 37.5760, "lon": 126.9769, "desc": "역사적인 궁궐, 한복 체험 지역"},
    {"name": "N Seoul Tower (남산서울타워)", "lat": 37.5512, "lon": 126.9882, "desc": "서울을 한눈에 볼 수 있는 전망 명소"},
    {"name": "Bukchon Hanok Village (북촌한옥마을)", "lat": 37.5826, "lon": 126.9830, "desc": "전통 한옥 거리"},
    {"name": "Changdeokgung Palace (창덕궁)", "lat": 37.5794, "lon": 126.9928, "desc": "유네스코 세계유산 궁궐"},
    {"name": "Myeongdong (명동 쇼핑거리)", "lat": 37.5626, "lon": 126.9860, "desc": "쇼핑과 길거리 음식의 중심지"},
    {"name": "Insadong (인사동)", "lat": 37.5744, "lon": 126.9850, "desc": "전통 차와 기념품 골목"},
    {"name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)", "lat": 37.5663, "lon": 127.0090, "desc": "현대 건축과 야시장·쇼핑"},
    {"name": "Hongdae / Hongik Univ. Area (홍대)", "lat": 37.5509, "lon": 126.9248, "desc": "젊음의 거리, 클럽·카페·스트리트 아트"},
    {"name": "Lotte World Tower & Mall (롯데월드타워)", "lat": 37.5126, "lon": 127.1026, "desc": "초고층 전망대와 쇼핑몰"},
    {"name": "Gwangjang Market (광장시장)", "lat": 37.5705, "lon": 126.9996, "desc": "전통 시장의 길거리 음식"},
]

# 기본 지도 (서울 중심)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for i, p in enumerate(PLACES, start=1):
    popup_html = f"<b>{i}. {p['name']}</b><br>{p['desc']}"
    folium.Marker(
        location=[p['lat'], p['lon']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=f"{i}. {p['name']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

st.subheader("지도 보기")
st.caption("마커를 클릭하면 장소 정보를 확인할 수 있습니다.")

# streamlit_folium의 st_folium을 사용해 Folium 맵을 렌더링
st_data = st_folium(m, width=1200, height=700)

st.markdown("---")
st.subheader("Top 10 장소 목록")
for i, p in enumerate(PLACES, start=1):
    st.markdown(f"**{i}. {p['name']}** — {p['desc']}  \n위도: {p['lat']}  경도: {p['lon']}")

st.info("이 앱은 Streamlit Community Cloud에 배포 가능한 예시입니다.")
