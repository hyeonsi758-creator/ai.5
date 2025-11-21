# Streamlit + Folium: 한국인이 좋아하는 해외 관광지 Top10 지도

아래는 **Streamlit Cloud**에서 바로 배포 가능한 코드(`app.py`)와 함께 `requirements.txt` 내용입니다. 파일 2개를 그대로 복사해서 Streamlit 앱으로 배포하세요.

---

## app.py

```python
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="한국인이 좋아하는 해외 관광지 Top10", layout="wide")
st.title("한국인이 좋아하는 해외 관광지 Top10 — 지도 표시")

st.markdown("간단한 지도 인터랙티브 앱입니다. 사이드바에서 옵션을 조정하세요.")

# Top10 관광지 데이터 (이름, 위도, 경도, 간단 설명, 순위)
places = [
    {"rank": 1, "name": "Shibuya Crossing (Tokyo, Japan)", "lat": 35.6595, "lon": 139.7005, "info": "도쿄의 상징적 교차로"},
    {"rank": 2, "name": "Dotonbori (Osaka, Japan)", "lat": 34.6687, "lon": 135.5013, "info": "오사카의 번화가, 음식 명소"},
    {"rank": 3, "name": "Taipei 101 (Taipei, Taiwan)", "lat": 25.033968, "lon": 121.564468, "info": "대만의 랜드마크 타이페이101"},
    {"rank": 4, "name": "Grand Palace (Bangkok, Thailand)", "lat": 13.7500, "lon": 100.4913, "info": "방콕의 역사적 궁전"},
    {"rank": 5, "name": "Victoria Peak (Hong Kong)", "lat": 22.2750, "lon": 114.1455, "info": "홍콩의 전망 명소"},
    {"rank": 6, "name": "Marina Bay Sands (Singapore)", "lat": 1.2834, "lon": 103.8607, "info": "싱가포르의 대표 호텔/전망"},
    {"rank": 7, "name": "Kuta Beach (Bali, Indonesia)", "lat": -8.7179, "lon": 115.1681, "info": "발리의 인기 해변"},
    {"rank": 8, "name": "Eiffel Tower (Paris, France)", "lat": 48.8584, "lon": 2.2945, "info": "파리의 상징, 에펠탑"},
    {"rank": 9, "name": "Tower Bridge (London, UK)", "lat": 51.5055, "lon": -0.0754, "info": "런던의 역사적 다리"},
    {"rank": 10, "name": "Ha Long Bay (Quang Ninh, Vietnam)", "lat": 20.9101, "lon": 107.1839, "info": "베트남의 자연 명소"},
]

# 사이드바 옵션
st.sidebar.header("옵션")
show_top_n = st.sidebar.slider("상위 몇 개 표시할까요?", min_value=1, max_value=10, value=10)
use_cluster = st.sidebar.checkbox("마커 클러스터 사용", value=True)

# 지도 초기 위치: 세계 중심
m = folium.Map(location=[20, 0], zoom_start=2)

if use_cluster:
    from folium.plugins import MarkerCluster
    cluster = MarkerCluster().add_to(m)

for p in places[:show_top_n]:
    popup_html = f"<b>{p['rank']}. {p['name']}</b><br>{p['info']}"
    # 첫 번째(1등)은 빨간색 아이콘
    icon_color = "red" if p['rank'] == 1 else "blue"
    marker = folium.Marker(
        location=[p['lat'], p['lon']],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=f"{p['rank']}. {p['name']}",
        icon=folium.Icon(color=icon_color, icon='info-sign')
    )
    if use_cluster:
        marker.add_to(cluster)
    else:
        marker.add_to(m)

# 지도 렌더링
st.subheader("지도")
st.write("마커를 클릭하면 관광지 정보를 볼 수 있습니다.")

# streamlit_folium의 st_folium을 사용해 Folium 맵을 렌더
st_data = st_folium(m, width=1200, height=700)

# 선택된 마커 정보가 있으면 우측 하단에 표시
if st_data and st_data.get("last_object_clicked"):
    click = st_data["last_object_clicked"]
    st.sidebar.write("마커 클릭 정보:")
    st.sidebar.json(click)

st.markdown("---")
st.markdown("**사용 방법**: 위 파일을 `app.py`로 저장하고 `requirements.txt`와 함께 Streamlit Cloud에 배포하세요.")
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

---

### 배포 팁

* Streamlit Cloud에 새 리포지토리를 연결하고 위 `app.py`와 `requirements.txt`를 넣으시면 자동으로 설치/배포됩니다.
* `streamlit_folium` 대신 직접 HTML으로 렌더링할 수도 있지만 `streamlit_folium`을 사용하면 상호작용이 편합니다.

*끝.*

