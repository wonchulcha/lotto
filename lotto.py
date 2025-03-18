import streamlit as st
import random
import os
from PIL import Image

st.title(':100:로또 번호 생성기')
st.write('##### ')
st.write('## 얼마나 사실라우:question:')
num_of_lines = st.number_input(' ',min_value=1000, max_value=100000, value=5000, step=1000)//1000
lucky_number = []

# CSS로 컬럼 레이아웃 고정
st.markdown("""
    <style>
    .css-1y0tads {  /* Streamlit의 columns 컨테이너 클래스 */
        display: flex;
        flex-wrap: nowrap;  /* 줄 바꿈 방지 */
        justify-content: space-between;
    }
    .css-1y0tads > div {  /* 각 컬럼 스타일 */
        flex: 1;  /* 동일한 너비로 고정 */
        min-width: 0;  /* 오버플로우 방지 */
    }
    </style>
""", unsafe_allow_html=True)


st.write('##### ')
if st.button('행운을 빌어요!!'):

  for i in range(num_of_lines):
    lucky_number.append(random.sample(range(1, 46), 6))
  # 각 줄의 번호를 이미지로 표시
  for i, line in enumerate(lucky_number):
      # 한 줄의 번호들을 가로로 나열
      if i % 5== 0:
        st.write('## 행운의 숫자')
      cols = st.columns(6)
      container = st.container()
      with container:
        for num, col in zip(sorted(line), cols):
            # 이미지 파일 경로
          img_path = f'numbers1_45/ball_{num}.png'
          
          try:
              image = Image.open(img_path)
              col.image(image, width=30)
          except:
              col.write(str(num))



