

### 키워드 검색 빈도별 데이터 분석

# -----------------------------------

import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import rcParams
from PIL import Image

# 그래프의 한글이 깨져서 복붙해옴-- 여전히 깨지는데...?? ==>> 해결 : 메인에서 폰트 설치
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')
# ------------------------------------


# -------------화면 배치 기획 --------------

# 키워드 검색 수 차트
# 인기 검색 키워드

# ------------------------------------------


#### 만약 컬럼이 알아보기 어렵다면 컬럼 설명을 붙여주도록 하자



def run_app_keyword():

    img = Image.open('data/library2-1.PNG')
    st.image(img)


    st.title('🌸도서 키워드 검색🌸')

    # st.markdown('#### 기본데이터')
    df = pd.read_csv('data/NL_AGE_ACCTO_BOOK_KWRD_LIST_202112.csv')

    # ### 1. 
    # st.text('원본 데이터를 확인하고싶다면 체크박스에 클릭 해 주세요')
    # if st.checkbox('데이터프레임 보기') :
    #     st.dataframe( df )

    ### 2.
        # 검색 빈도가 가장 많은 키워드를 보여주고싶은데
        # 유저가 원하는 랭크만큼 보여주고싶을떄
        # 숫자를 선택하면
        # 그 숫자에 해당하는 행 만큼만 나타나게 해보기

        # 기본 가공 데이터
    df1 = df.iloc[ : , 2: ]
    df2 = df1.rename(columns={'AGE_FLAG_NM' : '연령대', 'KWRD_RANK_CO':'키워드 순위 수' ,
                              'KWRD_NM': '키워드', 'FQ_CO':'검색 수', 'star':'별점' })
    
    # 검색 빈도 데이터프레임을 가져온다
    keyword_groupby = (df2.groupby('키워드')['검색 수'].sum()).sort_values(ascending = False)
    keyword_groupby = pd.DataFrame(keyword_groupby).reset_index()

    
    # 키워드 랭킹을 화면에 보여주기
    # 키워드 랭킹 데이터프레임 보여주기
    # 라인플롯 그래프 보여주기
    # 그래프는 그냥 띄워놓고 키워드 랭킹도 그냥 띄워놓고
    # 랭킹은 1,5,10,20 선택 가능하도록 만들기
    

    # st.subheader('키워드 검색 수 차트')
    # fig = plt.figure()
    # kwrd_rank = df2.loc[ : , : ].sort_values('검색 수', ascending = False)
    # sns.lineplot(data = kwrd_rank.head(30), 
    #          x = '키워드', y = '검색 수', hue = '연령대', style = '연령대')
    # plt.title('키워드 검색 수')
    # plt.xlabel('키워드')
    # plt.ylabel('검색 수')
    # st.pyplot(fig)

    st.subheader('키워드 검색 수 표로 보기')
    num = [1,5,10,20, 30]
    group_rank = st.selectbox('원하는 순위까지 숫자를 선택 해 주세요', num)
    st.dataframe( keyword_groupby.head(int(group_rank)) )


    




    ### 3.
    st.subheader('인기 검색 키워드')

    # 인기 검색 데이터 가져오기 ----------
    df1['FQ_CO']

    def get_point(FQ_CO):
        if FQ_CO >= 5000 :
            return 5
        elif FQ_CO >= 4000 :
            return 4
        elif FQ_CO >= 3000 :
            return 3
        elif FQ_CO >= 2000 :
            return 2
        elif FQ_CO >= 1000 :
            return 1
        else :
            return 0

    df1['star'] = df1['FQ_CO'].apply(get_point)
    # ------------------------------------


    st.text('검색수 1000건 이상의 인기 키워드만 보여드립니다.')
    st.text('검색량이 1000건 이상인 키워드에는 별1개, 2000천건 이상인 키워드에는 별2개')
    st.text('검색량이 3000건 이상인 키워드에는 별3개, 4000천건 이상인 키워드에는 별4개를 붙였습니다')

    num_list = [1,5,10,20]
    top_num = st.selectbox('보고싶은 순위까지 선택하세요', num_list)
    select_star = st.slider('원하시는 별의 개수를 선택해주세요', min_value = 1, max_value = 4, 
                    step = 1, value = 4 )
    
    # 컬럼 리네이밍
    df2 = df1.rename(columns={'AGE_FLAG_NM' : '연령대', 'KWRD_RANK_CO':'키워드 순위 수' ,'KWRD_NM': '키워드', 'FQ_CO':'검색 수', 'star':'별점' })
    
    # 별 개수 선택한 후 보고싶은 순위까지 보여주기
    df2_top = (df2.loc[   df2['별점'] == select_star ,    ]).head(int(top_num))
    df2_top = df2_top.sort_values('검색 수', ascending = False)

    # 앞에 인덱스는 떼고 보여주기
    df2_Top = df2_top.reset_index(drop=True)

    st.dataframe(   df2_Top    )






### 오류났었던 코드 -----------------------------------------------------------------------------

    # 별의 개수로 데이터 찾아서 보여주기
    # 멀티 셀렉트를 써야겠다

    # st.text('검색수 1000건 이상의 인기 키워드만 보여드립니다.')
    # st.text('검색량이 1000건 이상인 키워드에는 별1개, 2000천건 이상인 키워드에는 별2개')
    # st.text('검색량이 3000건 이상인 키워드에는 별3개, 4000천건 이상인 키워드에는 별4개를 붙였습니다')


    # age_list = ['20대', '30대', '40대', '50대', '60대 이상', '영유아(0~5)', '유아(6~7)',
    #     '청소년(14~19)', '초등(8~13)' ]
    # num_list = [1,2,3,4,5,6,7,8,9,10]


    # selcet_age = st.multiselect('원하는 연령대를 선택 해 주세요', age_list )
    # select_star = st.slider('원하시는 별의 개수를 선택해주세요', min_value = 1, max_value = 4, 
    #                 step = 1, value = 4 )
    # top_num = st.selectbox('보고싶은 키워드의 수', num_list )
        

    # step1 = df1['AGE_FLAG_NM'] == age_list
    # step2 = df1['star'] == str(select_star)


    # top_keyword = (  df1.loc[ step1 & step2,  ]  ).head(top_num)
    # st.dataframe(top_keyword)
    

    ## 이렇게 할 게 아니라 연령선택하는걸 빼자.

### -------------------------------------------------------------------------------------