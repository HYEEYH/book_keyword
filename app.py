

### 메인 구동 앱

# -----------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from app_home import run_app_home
from app_keyword import run_app_keyword
from app_age import run_app_age


## 그래프에 한글이 깨져서 설치함 ---
from matplotlib import font_manager, rc

# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)
# --------------------------------


from PIL import Image
# -----------------------------------


def main():

    # 메뉴 만들기
    # 메뉴는 몇개를 만들까

    menu = ['Home', '키워드', '연령대' ]
    st.sidebar.image('data/books_12.png', width=200)
    st.sidebar.title('메뉴')
    choice = st.sidebar.selectbox('가고싶은 페이지를 선택하세요', menu)


    if choice == menu[0] :
        run_app_home()

    elif choice == menu[1] :
        run_app_keyword()

    else:
        run_app_age()


if __name__ == '__main__':
    main()