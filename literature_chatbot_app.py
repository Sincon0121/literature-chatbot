import streamlit as st
from dotenv import load_dotenv
import os
import openai

# .env 파일 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="문학 작품 분석 & 추천 챗봇")
st.title("📚 문학 작품 분석 & 추천 챗봇")
st.markdown("""
작품 제목만 입력하면 AI가 분석해주고, 유사한 작품을 추천해줘요!
""")

# 사용자 입력 받기
user_input = st.text_input("분석할 문학 작품 제목을 입력하세요:", placeholder="예: 메밀꽃 필 무렵")

if st.button("분석 및 추천하기") and user_input.strip() != "":
    with st.spinner("분석 중입니다... ⏳"):

        # ChatGPT에 보낼 메시지 구성
        messages = [
            {"role": "system", "content": "너는 한국 문학 작품을 분석하는 비평가야. 사용자가 제목을 주면 작품의 주제, 정서, 등장인물 특징 등을 분석한 뒤 비슷한 한국 문학 작품을 추천해줘."},
            {"role": "user", "content": f"{user_input} 분석해줘"}
        ]

        try:
            # GPT 호출
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )

            result = response['choices'][0]['message']['content']
            st.success("✅ 분석 결과")
            st.markdown(result)

        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")

else:
    st.info("작품 제목을 입력하고 버튼을 눌러주세요.")