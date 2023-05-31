


# -----------------------------------

import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from app_home import run_app_home
from app_eda import run_app_eda

from PIL import Image
# -----------------------------------


def main():

    # 메뉴 만들기
    # 메뉴는 몇개를 만들까
    # 
    menu = ['Home', 'EDA']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_app_home()

    else:
        run_app_eda()


if __name__ == '__main__':
    main()