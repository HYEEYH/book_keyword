
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


from PIL import Image
# -----------------------------------


def main():

    # 메뉴 만들기
    # 메뉴는 몇개를 만들까
    # 
    menu = ['Home', '키워드', '연령대' ]
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_app_home()

    elif choice == menu[1] :
        run_app_keyword()

    else:
        run_app_age()


if __name__ == '__main__':
    main()