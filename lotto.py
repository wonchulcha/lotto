import streamlit as st
import random
import os
from PIL import Image
import base64
import io

# HTML과 CSS를 사용하여 모바일에서도 6개 이미지가 한 행에 표시되도록 설정
st.markdown("""
<style>
    /* 더 강력한 스타일링을 위해 !important 사용 */
    /* 기존 컬럼 스타일 재정의 */
    div.stHorizontalBlock, 
    div.row-widget.stHorizontalBlock,
    div[data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        flex-direction: row !important;
        display: flex !important;
    }
    
    /* 커스텀 행 스타일 */
    .lotto-row {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: flex-start !important;
        align-items: center !important;
        margin-bottom: 20px !important;
        overflow-x: auto !important;
        width: 100% !important;
    }
    
    .lotto-ball {
        flex: 0 0 auto !important;
        width: 80px !important;
        height: 80px !important;
        margin-right: 15px !important;
        text-align: center !important;
    }
    
    .lotto-ball img {
        width: 80px !important;
        height: 80px !important;
        max-width: 100% !important;
        object-fit: contain !important;
    }
    
    .lotto-number {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 80px !important;
        height: 80px !important;
        border-radius: 50% !important;
        background-color: #FFD700 !important;
        color: #000 !important;
        font-weight: bold !important;
        font-size: 24px !important;
        margin: 0 auto !important;
    }
    
    /* 모바일 화면에서는 크기 조정 */
    @media (max-width: 640px) {
        /* 스트림릿 기본 스타일 무시 */
        div[data-testid="stVerticalBlock"] > div {
            flex-direction: row !important;
        }
        
        .lotto-ball {
            width: 40px !important;
            height: 40px !important;
            margin-right: 10px !important;
        }
        
        .lotto-ball img {
            width: 40px !important;
            height: 40px !important;
        }
        
        .lotto-number {
            width: 40px !important;
            height: 40px !important;
            font-size: 16px !important;
        }
        
        .lotto-row {
            padding-bottom: 5px !important;
            margin-bottom: 10px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# 이미지를 base64로 인코딩하는 함수
def get_image_base64(img_path):
    try:
        with Image.open(img_path) as img:
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return f"data:image/png;base64,{img_str}"
    except Exception:
        return None

# 모든 이미지를 미리 로드
def load_all_ball_images():
    ball_images = {}
    for num in range(1, 46):
        img_path = f'numbers1_45/ball_{num}.png'
        img_data = get_image_base64(img_path)
        if img_data:
            ball_images[num] = img_data
    return ball_images

st.title(':100:로또 번호 생성기')
st.write('## 얼마나 사실라우:question:')
num_of_lines = st.number_input(' ',min_value=1000, max_value=100000, value=5000, step=1000)//1000
lucky_number = []

if st.button('행운을 빌어요!!'):
    # 모든 이미지 미리 로드
    ball_images = load_all_ball_images()
    
    for i in range(num_of_lines):
        lucky_number.append(random.sample(range(1, 46), 6))
    
    # 각 줄의 번호를 이미지로 표시
    for i, line in enumerate(lucky_number):
        # 한 줄의 번호들을 가로로 나열
        if i % 5 == 0:
            st.write('## 행운의 숫자')
        
        # HTML로 한 행에 6개 이미지 표시
        html_row = '<div class="lotto-row">'
        
        for num in sorted(line):
            if num in ball_images:
                # 이미지 있을 경우 이미지 사용
                html_row += f'<div class="lotto-ball"><img src="{ball_images[num]}" alt="{num}"></div>'
            else:
                # 이미지 없을 경우 스타일링된 숫자 표시
                html_row += f'<div class="lotto-ball"><div class="lotto-number">{num}</div></div>'
        
        html_row += '</div>'
        st.markdown(html_row, unsafe_allow_html=True)



