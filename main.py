import pandas as pd

url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

# 데이터 확인
print(df.head())
import plotly.express as px

# 예: x = '날짜', y = '값', color = '카테고리'
fig = px.line(df, x='날짜', y='값', color='카테고리', title='카테고리별 값 변화')
fig.show()
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 데이터 시각화 웹앱")

url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

st.write("데이터 미리보기:")
st.dataframe(df)

# 예시: 사용자가 컬럼 선택해서 시각화
x_axis = st.selectbox("X축 선택", df.columns)
y_axis = st.selectbox("Y축 선택", df.columns)

fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
st.plotly_chart(fig)
