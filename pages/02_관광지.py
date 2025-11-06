import streamlit as st
from streamlit_folium import st_folium
import folium

# 페이지 설정
st.set_page_config(page_title="서울 외국인 인기 관광지 TOP10", layout="wide")

# 제목
st.title("🌏 서울 외국인 인기 관광지 TOP10 🇰🇷")
st.markdown("서울을 방문하는 외국인 관광객에게 특히 인기 있는 명소 10곳을 지도에 표시했습니다.")

# 관광지 데이터
PLACES = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.5760, "lon": 126.9769, "desc": "조선의 법궁으로, 아름다운 건축과 역사 체험이 가능한 장소입니다."},
    {"name": "남산서울타워 (N Seoul Tower)", "lat": 37.5512, "lon": 126.9882, "desc": "서울 전경을 한눈에 볼 수 있는 전망대이며, 야경이 특히 아름답습니다."},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.5826, "lon": 126.9830, "desc": "전통 한옥이 잘 보존된 거리로, 한복 체험과 사진 명소로 유명합니다."},
    {"name": "창덕궁 (Changdeokgung Palace)", "lat": 37.5794, "lon": 126.9928, "desc": "유네스코 세계문화유산으로 지정된 조선시대 궁궐입니다."},
    {"name": "명동 쇼핑거리 (Myeongdong Shopping Street)", "lat": 37.5626, "lon": 126.9860, "desc": "패션, 화장품, 길거리 음식 등으로 외국인 관광객에게 인기 있는 쇼핑 지역입니다."},
    {"name": "인사동 (Insadong)", "lat": 37.5744, "lon": 126.9850, "desc": "전통 찻집과 기념품 상점이 많은 서울의 대표적인 문화거리입니다."},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5663, "lon": 127.0090, "desc": "미래적인 건축물과 다양한 전시, 야시장으로 유명한 복합 문화 공간입니다."},
    {"name": "홍대 거리 (Hongdae Area)", "lat": 37.5509, "lon": 126.9248, "desc": "젊음의 거리로, 거리공연·카페·클럽·예술적 분위기로 가득한 지역입니다."},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.5126, "lon": 127.1026, "desc": "555m 초고층 건물로, 전망대·쇼핑몰·호텔이 함께 있는 랜드마크입니다."},
    {"name": "광장시장 (Gwangjang Market)", "lat": 37.5705, "lon": 126.9996, "desc": "빈대떡, 마약김밥 등 다양한 전통 먹거리를 즐길 수 있는 서울의 대표 전통시장입니다."},
]

# 지도 생성 (서울 중심)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles="OpenStreetMap")

# 관광지 마커 추가
for i, place in enumerate(PLACES, start=1):
    popup_html = f"<b>{i}. {place['name']}</b><br>{place['desc']}"
    folium.Marker(
        location=[place['lat'], place['lon']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=f"{i}. {place['name']}",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st.subheader("🗺️ 관광지 지도")
st.caption("마커를 클릭하면 관광지 정보를 볼 수 있습니다.")
st_folium(m, width=1200, height=700)

# 관광지 목록
st.markdown("---")
st.subheader("📍 관광지 목록")
for i, place in enumerate(PLACES, start=1):
    st.markdown(f"**{i}. {place['name']}**  \n{place['desc']}  \n위도: {place['lat']} / 경도: {place['lon']}")

# 하단 정보
st.markdown("---")
st.success("이 앱은 Streamlit Community Cloud에서 실행할 수 있는 예시입니다.")
st.caption("※ 데이터 출처: VisitSeoul, TripAdvisor, Wikipedia 등을 참고하여 작성되었습니다.")
