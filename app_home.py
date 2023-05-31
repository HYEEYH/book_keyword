


# -----------------------------------

import streamlit as st

from PIL import Image
# -----------------------------------



def run_app_home():
    st.title('도서 키워드 검색')
    st.header('도서 키워드 검색 앱에 오신걸 환영합니다.')
    st.text('국립 중앙 도서관 제공 연령별 도서 키워드를 토대로')
    st.text('원하시는 연령대에서 가장 많이 검색한 도서 키워드를 알려드립니다.')

    img = Image.open('data/NL1.jpg')
    st.image(img)