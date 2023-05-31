


# -----------------------------------

import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import font_manager, rc
from matplotlib import rcParams

from PIL import Image
# -----------------------------------


# -------------화면 배치 기획 --------------

# 도서 키워드 검색
#### 이곳에서 키워드의 여러 데이터 분석을 보실 수 있습니다.

## 데이터 프레임 보기
## 연간 키워드 검색 순위
## 연령대별 키워드 검색 순위
## 키워드 검색 빈도
### 키워드 검색 빈도수가 1000건 이상인 데이터
### 키워드를 가장 많이 검색한 연령대



# ------------------------------------------


def run_app_eda():
    st.title('도서 키워드 검색')

    st.subheader('기본 데이터')
    df = pd.read_csv('data/NL_AGE_ACCTO_BOOK_KWRD_LIST_202112.csv')

    st.text('')
    if st.checkbox('데이터프레임 보기') :
        st.dataframe( df )
