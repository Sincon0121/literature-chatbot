import streamlit as st

# 🔹 사용자 입력 파싱 함수
def parse_input(text):
    data = {}
    lines = text.strip().split("\n")
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data

# 🔹 작품 분석 출력 함수
def analyze_work(data):
    return f"""
📖 작품 분석 결과

- 제목: {data.get('제목')}
- 작가: {data.get('작가')}
- 등장인물: {data.get('등장인물')}
- 작품 상황: {data.get('상황')}
- 정서 및 표현기법: {data.get('정서 및 표현기법')}

📝 이 작품은 '{data.get('정서 및 표현기법')}'을 통해 '{data.get('상황')}'을 인상적으로 전달합니다.
"""

# 🔹 추천 작품 함수
def recommend_next_work(expression_style):
    themes = {
        "서정적": ["소나기 - 황순원", "엄마의 말뚝 - 박완서"],
        "풍자적": ["날개 - 이상", "운수 좋은 날 - 현진건"],
        "향토적": ["동백꽃 - 김유정", "봄봄 - 김유정"],
        "역사적 비극": ["장마 - 윤흥길", "삼포 가는 길 - 황석영"],
        "자연 묘사": ["메밀꽃 필 무렵 - 이효석", "산골 아이 - 이청준"]
    }

    for keyword, works in themes.items():
        if keyword in expression_style:
            return f"📚 추천 작품: {works[0]}"
    return "📚 추천 작품: 운수 좋은 날 - 현진건 (기본 추천)"

# 🔹 Streamlit 앱 UI
st.title("📚 문학 작품 분석 & 추천 챗봇")

st.markdown(
    '''작품 정보를 아래 형식에 맞게 입력하세요:

제목: 메밀꽃 필 무렵  
작가: 이효석  
등장인물: 허생원, 동이, 조선달  
상황: 허생원이 장터에서 만난 동이와의 대화 속에서 과거를 회상하고, 결국 동이와 특별한 관계임을 암시  
정서 및 표현기법: 향토적 정서, 서정적 문체, 자연 묘사  
'''
)

# 🔹 사용자 입력
user_input = st.text_area("작품 정보를 입력하세요:", height=250)

# 🔹 분석 버튼
if st.button("분석 및 추천하기"):
    if user_input.strip() == "":
        st.warning("⚠️ 작품 정보를 입력해 주세요.")
    else:
        data = parse_input(user_input)
        st.markdown(analyze_work(data))
        st.success(recommend_next_work(data.get("정서 및 표현기법", "")))