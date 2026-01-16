import streamlit as st
import random
import time

# 1. 페이지 설정: 최대한 조잡하게!
st.set_page_config(page_title="🎢경주월드: 샤갈&두쫀쿠🎢", layout="wide")

# 2. 미친 비주얼 CSS (눈뽕 주의)
st.markdown("""
    <style>
    @keyframes party {
        0% { background-color: #ff00ff; }
        25% { background-color: #00ff00; }
        50% { background-color: #ffff00; }
        75% { background-color: #00ffff; }
        100% { background-color: #ff00ff; }
    }
    .stApp {
        animation: party 0.5s infinite; /* 배경 무한 깜빡이 */
        opacity: 0.9;
    }
    .shagal-text {
        font-size: 100px !important;
        color: #FFFFFF !important;
        font-weight: 900;
        text-shadow: 10px 10px #FF0000, -10px -10px #0000FF;
        text-align: center;
        transform: skewY(-5deg);
    }
    .stButton>button {
        border-radius: 0px !important;
        border: 10px double white !important;
        font-family: 'Comic Sans MS', cursive;
        font-size: 25px !important;
        height: 100px !important;
    }
    .stButton>button:active {
        transform: scale(0.5) rotate(360deg);
    }
    marquee {
        background-color: black;
        color: yellow;
        font-family: 'Courier New';
        font-size: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 텍스트 테러
st.markdown("<marquee>📢 샤갈~! 샤갈~! 두쫀쿠!! 두쫀쿠!! 누구라예?? 리으을~~?? 📢</marquee>", unsafe_allow_html=True)
st.markdown('<p class="shagal-text">🎢경주월드🎢</p>', unsafe_allow_html=True)

# 4. 사이드바 - 정신 나간 필터
with st.sidebar:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3YmaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKMGpx6v2G1ADqE/giphy.gif")
    st.header("🤪 샤갈~ 지수 측정")
    st.slider("오늘 얼마나 샤갈스러운가요?", 0, 1000, 500)
    if st.button("두쫀쿠!! 버튼"):
        st.error("💥 두쫀쿠!! 폭발!! 💥")
        st.balloons()

# 5. 메인 레이아웃 (난장판 4분할)
st.write("### 💸 조롱하려면 일단 입금부터 (샤갈~!)")

members = [
    {"name": "이수민", "mbti": "ISFJ", "nick": "남한길", "bank": "카카오뱅크 3333-13-2239193", "taunt": "길 잃은 남한길에게 한 줄기 빛(돈)을..."},
    {"name": "김경아", "mbti": "ENTP", "nick": "발렛파킹", "bank": "카카오뱅크 3333-12-1244746", "taunt": "발렛비 안 내면 네 차는 이제 제 겁니다."},
    {"name": "강서현", "mbti": "ISFP", "nick": "캉다시마", "bank": "카카오뱅크 3333-15-6915803", "taunt": "다시마처럼 끈덕지게 조롱받을 준비 완료!"},
    {"name": "윤혜빈", "mbti": "ESFP", "nick": "수진이", "bank": "카카오페이 010-8789-4037", "taunt": "수진아!! 입금 확인되면 조롱 시작한다?"}
]

cols = st.columns(4)

for i, m in enumerate(members):
    with cols[i]:
        st.markdown(f"""
            <div style="background: white; color: black; padding: 10px; border: 5px solid red;">
                <h4>{m['name']}</h4>
                <p>MBTI: {m['mbti']}<br>별명: {m['nick']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🖕 {m['name']} 조롱"):
            st.toast(f"샤갈~! {m['name']} 조롱 대기 중...")
            st.warning(f"👉 {m['taunt']}")
            st.write("**조롱하려면 입금하세요(복사하기)**")
            st.code(m['bank'])
            if st.button(f"{m['name']}에게 샤갈~!"):
                st.snow()

st.write("---")

# 6. 샤갈~! 두쫀쿠!! 전용 사운드 보드 (텍스트 버전)
st.header("🔊 경주월드 공식 추임새")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("샤갈~!"):
        st.markdown("# 🌊 샤! 갈~!")
        st.balloons()

with c2:
    if st.button("두쫀쿠!!"):
        st.markdown("# 🍪 두! 쫀! 쿠!!")
        st.warning("두툼하고 쫀득한 쿠키 아님 주의")

with c3:
    if st.button("리으을~?"):
        st.markdown("# 🤪 리으으으으을~~?")

with c4:
    if st.button("누구라예?"):
        st.markdown("# 🧐 누구라예?!?!")

# 7. 무근본 갤러리 & 현생 찌들기 구역
st.write("---")
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📸 뒷태 브이 인증샷 (거지 전용)")
    st.camera_input("뒷태 브이 찍어라 거지들아")

with col_right:
    st.subheader("👵 할매조끼 대여소")
    if st.button("할매조끼 랜덤 대여"):
        v_types = ["꽃무늬 누빔", "겨자색 모직", "갈색 체크", "정체불명 보라색"]
        st.success(f"당신은 오늘 '{random.choice(v_types)} 조끼' 당첨!")
        st.write("샤갈~하게 잘 어울리시네요!")

# 8. 바닥 (끝까지 정신없게)
st.write("---")
if st.button("마지막으로 한마디"):
    for _ in range(3):
        st.write("### 🎢 경주월드는 영원하다!!! 샤갈~!!!")
        time.sleep(0.1)
    st.write("# 💥 두 쫀 쿠 💥")