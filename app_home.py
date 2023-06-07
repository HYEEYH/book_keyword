

### 홈 화면 구성

# -----------------------------------

import streamlit as st
import pandas as pd

from PIL import Image

## 화면 레이아웃 구성 라이브러리

# -----------------------------------


def run_app_home():

        img = Image.open('data/library2-1.PNG')
        st.image(img)
   
        st.title('도서 키워드 검색')
        st.header('도서키워드앱에 오신걸 환영합니다')
        st.text('국립 중앙 도서관 제공 연령별 도서 키워드를 토대로')
        st.text('사람들이 가장 많이 검색한 도서 키워드를 알려드립니다.')

        img = Image.open('data/NL1.jpg')
        st.image(img)


#### 만약 컬럼이 알아보기 어렵다면 컬럼 설명을 붙여주도록 하자