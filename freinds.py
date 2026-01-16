import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="🎢경주월드!!!🎢", layout="wide")

# 배경색과 폰트 흔들기 효과 (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #FF00FF;
    }
    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      20% { transform: translate(-3px, 0px) rotate(1deg); }
      30% { transform: translate(3px, 2px) rotate(0deg); }
      40% { transform: translate(1px, -1px) rotate(1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
    }
    .shake-text {
        display: inline-block;
        animation: shake 0.5s infinite;
        font-size: 50px !important;
        color: yellow !important;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background-color: #00FF00;
        color: black;
        border: 5px dotted red;
    }
    </style>
    """, unsafe_allow_html=True)

# 헤더 - 정신나간 타이틀
st.markdown('<div class="shake-text">🎢💥 경주월드 입장 💥🎢</div>', unsafe_allow_html=True)
st.write("### 🚨 주의: 정신이 혼미해질 수 있음 🚨")

# 사이드바에도 아무말 대잔치
with st.sidebar:
    st.error("현생 찌들기 금지!!")
    st.warning("거지 환영")
    if st.button("누구라예?"):
        st.balloons()
    st.text_input("조롱할 사람 입력", "윤혜빈")

# 메인 레이아웃 - 난잡하게 쪼개기
col1, col2, col3, col4 = st.columns([1, 2, 1, 1])

with col1:
    st.subheader("👴 할매조끼 존")
    st.button("리으을~?")
    st.image("https://placekitten.com/200/300") # 무근본 고양이 사진

with col2:
    st.subheader("👥 멤버 프로필 (개판)")
    members = [
        {"이름": "이수민", "MBTI": "ISFJ", "별명": "남한길"},
        {"이름": "김경아", "MBTI": "ENTP", "별명": "발렛파킹"},
        {"이름": "강서현", "MBTI": "ISFP", "별명": "캉다시마"},
        {"이름": "윤혜빈", "MBTI": "ESFP", "별명": "수진이"}
    ]
    
    for m in members:
        with st.expander(f"🔥 {m['이름']} (클릭하면 폭발)"):
            st.write(f"**별명:** {m['별명']}")
            st.write(f"**MBTI:** {m['MBTI']}")
            if st.button(f"{m['이름']} 조롱하기"):
                st.snow()

with col3:
    st.subheader("✨ 특기 목록")
    skills = ["뒷태 브이", "남 조롱하기", "현생 찌들기", "거지", "할매조끼", "리으을~", "누구라예?"]
    for skill in skills:
        st.checkbox(skill, value=True)

with col4:
    st.subheader("💣 버튼 지옥")
    for i in range(5):
        st.button(f"의미없는 버튼 {i}")

# 하단부 - 난장판 마무리
st.markdown("---")
if st.button("현생 탈출 버튼"):
    st.write("# 🏃‍♂️🏃‍♀️💨💨💨")
    st.success("경주월드 멤버들은 현재 도망 중입니다.")

# 랜덤 문구 출력
st.info(random.choice(["누구라예??", "리으을~~?", "뒷태 브이 브이!", "거지들 모임.."]))