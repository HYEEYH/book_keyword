

### 연령대별 데이터분석

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
## 연령대별 키워드 검색 순위
## 키워드를 가장 많이 검색한 연령대


# ------------------------------------------


#### 만약 컬럼이 알아보기 어렵다면 컬럼 설명을 붙여주도록 하자



def run_app_age():

    
    img = Image.open('data/library2-1.PNG')
    st.image(img)


    st.title('도서 키워드 검색')


    ### 1.
    # st.markdown('#### 기본데이터')
    df = pd.read_csv('data/NL_AGE_ACCTO_BOOK_KWRD_LIST_202112.csv')
    # st.text('')
    # if st.checkbox('데이터프레임 보기') :
    #     st.dataframe( df )




    # 기본 가공 데이터
    df1 = df.iloc[ : , 2: ]
    df2 = df1.rename(columns={'AGE_FLAG_NM' : '연령대', 'KWRD_RANK_CO':'키워드 순위 수' ,
                              'KWRD_NM': '키워드', 'FQ_CO':'검색 수', 'star':'별점' })




    ### 2.
    st.subheader('연령대 별 인기 키워드')
    st.text('연령대 별 인기 키워드를 보여드립니다')

    age_list = ['20대', '30대', '40대', '50대', '60대 이상', '영유아(0~5)', 
                '유아(6~7)','청소년(14~19)', '초등(8~13)' ]
    num_list = [1,5,10,20]

    select_age = st.selectbox('연령대를 선택 하세요', age_list)
    select_rank = st.selectbox('보고싶은 순위까지 선택하세요', num_list)


    st.dataframe( (df2.loc[ df2['연령대'] == select_age , ]).head(int(select_rank))     )







    ### 3. 
    st.subheader('이 키워드를 가장 많이 선택한 연령대는?')
    st.text('내가 선택한 키워드를 가장 많이 검색한 연령대를 알려드립니다')

    # 키워드를 리스트로 만든 데이터
    # df1_unique = df1['KWRD_NM'].unique().tolist()


    key_list = df1_unique = df2['키워드'].unique().tolist()
    num_list = [1,5,10,20]


    select_keyword = st.selectbox('키워드를를 선택 하세요', key_list)
    # select_rank1 = st.selectbox('보고싶은 순위까지 선택하세요', num_list)


    data1 = (df2.loc[ df2['키워드'] == select_keyword , ]).sort_values('검색 수', ascending = False)
    data1 = data1.iloc[ : , : ]


    # 인덱스가 붙어있어서 인덱스만 떨어뜨림
    data = data1.reset_index(drop=True)
    
    
    st.dataframe( data )
