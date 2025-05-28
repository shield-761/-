import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("📊 Google Drive CSV 시각화 대시보드")

# 데이터 로드
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df)

# 컬럼 선택
st.subheader("Plotly 그래프 그리기")

numeric_columns = df.select_dtypes(include='number').columns.tolist()
if len(numeric_columns) < 2:
    st.warning("시각화를 위해 두 개 이상의 수치형 컬럼이 필요합니다.")
else:
    x_axis = st.selectbox("X축", numeric_columns)
    y_axis = st.selectbox("Y축", numeric_columns, index=1 if len(numeric_columns) > 1 else 0)

    # Plotly 시각화
    fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
    st.plotly_chart(fig)
