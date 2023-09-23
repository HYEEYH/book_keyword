![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Book%20Keyword&fontSize=70)

# book_keyword
개인프로젝트 - 책 키워드 분석 앱 대시보드
<br/><br/>
* 어떤 책 키워드가 가장 검색이 많았는지, 연령대 별로 책 인기 키워드는 어떻게 다른지 보여주는 앱 대시보드 입니다.<br/>
- 내가 검색한 키워드를 어떤 연령대가 가장 많이 검색했는지 알려줄 수 있는 앱 대시보드
- 검색 빈도가 높은 인기 키워드를 가장 높은 순서부터 보여줌.
- 나이대별로 가장 검색이 많았던 키워드를 보여줌.
<br/>
<a href= "https://drive.google.com/file/d/1bB3lG-ItFfgfPVFq5QEewgbJ82xf6GGP/view?usp=drive_link">[시연 영상 보러 가기]</a><br/><br/>
<img src="https://github.com/HYEEYH/aws-rekognition-app2/assets/130967557/486a902c-5c7f-46de-b0c0-da62bfe420a9"  width="700" height="668" /><br/><br/>

## 사용 툴
<div align=center>
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white"/>
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white"/>
<img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"> 
</div>

## 사용한 기술
### Back-ends
#### Visual Studio Code (Python)
##### Streamlit
- 데이터를 불러오고, 불러온 데이터를 데이터 프레임과 차트로 표현
- 키워드의 검색 순위를 유저가 선택할 수 있도록 함
- 연령대와 키워드를 입력받아 해당 연령대에서 선택된 키워드가 몇위인지를 보여줌.
- 라디오 버튼과 드롭다운박스를 이용하여 유저에게 원하는 구매 예측을 원하는 항목(컬럼)을 입력 받음.
- 유저에게 입력 받은 정보를 가지고 regressor 사용하여 구매 예측 실행
#### AWS
- AWS EC2를 서버로 활용해 앱 대시보드 제작

#### 데이터 분석 - 구글 코랩(Google Colab)
##### 데이터 전처리
- Numfy와 Pandas를 이용해 데이터 통계 처리
- 원하는 컬럼만 뽑아서 가져옴
- 키워드를 기준으로 그룹바이 사용하여 해당 키워드의 총 검색 수를 도출
- 키워드의 검색 수를 기준으로 정렬
- 영문 줄임말로 되어있는 컬럼을 한글로 변환
- 키워드 검색수가 1000건이 넘어가는 데이터만 따로 구함
- 두 컬럼에 원하는 조건을 각각 걸어 원하는 정보를 구함
- 유니크를 사용해 중복없이 연령대, 중복없는 키워드를 가져와 리스트로 저장
- matplotlib을 이용하여 나이대별 키워드 검색 수와 연령대 별 1위 키워드만 그래프로 표현
- concat을 사용하여 데이터 이어붙임



##### 
<br/><br/><br/>
