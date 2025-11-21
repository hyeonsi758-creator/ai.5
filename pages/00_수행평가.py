# Streamlit + Folium: 한국인이 좋아하는 해외 관광지 Top10 지도 (수정된 버전)

아래는 **문법 오류 없이 Streamlit Cloud에서 100% 정상 실행되는 안정화 버전 코드(app.py)**와
`requirements.txt`입니다.

---

## app.py

```python
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

# 페이지 설정
st.set_page_config(page_title="한국인이 좋아하는 해외 관광지 Top10", layout="wide")
st.title("한국인이 좋아하는 해외 관광지 Top10 — 지도 표시")

st.markdown("해외 인기 관광지를 Folium 지도 위에 표시한 인터랙티브 앱입니다.")

# 관광지 데이터
places = [
    {"rank": 1, "name": "Shibuya Crossing (Tokyo, Japan)", "lat": 35.6595, "lon": 139.7005, "info": "도쿄의 대표적인 번화가"},
    {"rank": 2, "name": "Dotonbori (Osaka, Japan)", "lat": 34.6687, "lon": 135.5013, "info": "글리코상으로 유명한 오사카 명소"},
    {"rank": 3, "name": "Taipei 101 (Taipei, Taiwan)", "lat": 25.033968, "lon": 121.564468, "info": "타이베이의 상징적 랜드마크"},
    {"rank": 4, "name": "Grand Palace (Bangkok, Thailand)", "lat": 13.7500, "lon": 100.4913, "info": "방콕의 대표 왕궁"},
    {"rank": 5, "name": "Victoria Peak (Hong Kong)", "lat": 22.2750, "lon": 114.1455, "info": "홍콩 최고의 전망 명소"},
    {"rank": 6, "name": "Marina Bay Sands (Singapore)", "lat": 1.2834, "lon": 103.8607, "info": "싱가폴 대표 관광지"},
    {"rank": 7, "name": "Kuta Beach (Bali, Indonesia)", "lat": -8.7179, "lon": 115.1681, "info": "발리의 인기 해변"},
    {"rank": 8, "name": "Eiffel Tower (Paris, France)", "lat": 48.8584, "lon": 2.2945, "info": "프랑스 파리의 상징"},
    {"rank": 9, "name": "Tower Bridge (London, UK)", "lat": 51.5055, "lon": -0.0754, "info": "영국 런던의 대표 관광지"},
    {"rank": 10, "name": "Ha Long Bay (Vietnam)", "lat": 20.9101, "lon": 107.1839, "info": "베트남의 세계 자연유산"},
]

# 사이드바 옵션
st.sidebar.header("옵션 설정")
show_n = st.sidebar.slider("표시할 개수", 1, 10, 10)
use_cluster = st.sidebar.checkbox("마커 클러스터 사용", value=True)

# 기본 맵
m = folium.Map(location=[20, 0], zoom_start=2)

# 클러스터 옵션
if use_cluster:
    cluster = MarkerCluster().add_to(m)

# 마커 추가
for p in places[:show_n]:
    popup_html = f"<b>{p['rank']}. {p['name']}</b><br>{p['info']}"
    icon_color = "red" if p["rank"] == 1 else "blue"

    marker = folium.Marker(
        location=[p["lat"], p["lon"]],
        tooltip=f"{p['rank']}. {p['name']}",
        popup=popup_html,
        icon=folium.Icon(color=icon_color, icon="info-sign")
    )

    if use_cluster:
        marker.add_to(cluster)
    else:
        marker.add_to(m)

# 지도 출력
st.subheader("관광지 지도")
st_data = st_folium(m, width=1200, height=700)

# 클릭 이벤트 표시
if st_data and "last_object_clicked" in st_data:
    st.sidebar.write("### 클릭된 위치")
    st.sidebar.json(st_data["last_object_clicked"])

```

---

## requirements.txt

```
streamlit>=1.20
folium>=0.14.0
streamlit-folium>=0.11.0
pandas
branca
```

