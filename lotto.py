import streamlit as st
import random
import os
from PIL import Image

st.title(':100:로또 번호 생성기')
st.write('##### ')
st.write('## 얼마나 사실라우:question:')
num_of_lines = st.number_input(' ',min_value=1000, max_value=100000, value=5000, step=1000)//1000
lucky_number = []
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
      
      for num, col in zip(sorted(line), cols):
          # 이미지 파일 경로
          img_path = f'numbers1_45/ball_{num}.png'
          
          try:
              image = Image.open(img_path)
              col.image(image, width=10)
          except:
              col.write(str(num))



