import streamlit as st
import random
import time

# 1. 페이지 설정 (최대한 무근본하게)
st.set_page_config(page_title="🎢경주월드: 샤갈&두쫀쿠🎢", layout="wide")

# 2. 광기의 CSS (무지개 깜빡이 + 흔들리는 버튼 + 굴러가는 텍스트)
st.markdown("""
    <style>
    @keyframes blink {
        0% { background-color: #ff00ff; }
        33% { background-color: #00ffff; }
        66% { background-color: #ffff00; }
        100% { background-color: #ff00ff; }
    }
    .stApp {
        animation: blink 0.2s infinite; /* 광속 깜빡이 */
        opacity: 0.8;
    }
    .main-title {
        font-size: 80px !important;
        font-weight: 900;
        color: #ff0000 !important;
        text-shadow: 5px 5px #fff, 10px 10px #000;
        text-align: center;
        animation: shake 0.1s infinite;
    }
    @keyframes shake {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        50% { transform: translate(-1px, -2px) rotate(-1deg); }
        100% { transform: translate(1px, 1px) rotate(0deg); }
    }
    .stButton>button {
        width: 100%;
        height: 70px;
        background-color: #000 !important;
        color: #0f0 !important;
        border: 5px solid #f0f !important;
        font-size: 20px !important;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #fff !important;
        color: #f0f !important;
        transform: scale(1.1) rotate(5deg);
    }
    marquee {
        font-size: 30px;
        color: yellow;
        background: black;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 굴러가는 텍스트 (Marquee)
st.markdown("<marquee>🔥 샤갈~! 샤갈~! 두쫀쿠!! 두쫀쿠!! 누구라예?? 리으을~~?? 뒷태 브이!! 🔥</marquee>", unsafe_allow_html=True)
st.markdown('<h1 class="main-title">🎢경주월드🎢</h1>', unsafe_allow_html=True)

# 4. 사이드바 - 현생 금지 구역
with st.sidebar:
    st.title("💸 거지 수용소")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3Y1b3YmaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKMGpx6v2G1ADqE/giphy.gif")
    if st.button("두쫀쿠!! 랜덤 박스"):
        st.balloons()
        st.error("당첨: 오늘 점심 굶기 (거지 지수 상승)")
    
    st.write("---")
    st.subheader("👵 할매조끼 대여소")
    if st.button("오늘의 조끼 뽑기"):
        st.info(f"오늘의 조끼: {random.choice(['빨간 꽃무늬', '갈색 체크', '겨자색 누빔', '보라색 할매조끼'])}")

# 5. 메인 레이아웃 (멤버별 조롱 & 입금 구역)
st.write("## 🤡 조롱하려면 입금하세요 (복사하기 버튼 있음)")

members = [
    {"name": "이수민", "mbti": "ISFJ", "nick": "남한길", "bank": "카카오뱅크 3333-13-2239193", "msg": "남한길처럼 길 잃기 전에 입금해 샤갈~!"},
    {"name": "김경아", "mbti": "ENTP", "nick": "발렛파킹", "bank": "카카오뱅크 3333-12-1244746", "msg": "발렛비 입금 안 하면 차 견인한다 두쫀쿠!!"},
    {"name": "강서현", "mbti": "ISFP", "nick": "캉다시마", "bank": "카카오뱅크 3333-15-6915803", "msg": "다시마처럼 끈적하게 조롱받을 준비 됐니?"},
    {"name": "윤혜빈", "mbti": "ESFP", "nick": "수진이", "bank": "카카오페이 010-8789-4037", "msg": "수진아!! 입금 확인 안 되면 조롱 금지다 샤갈~!"}
]

# 4열로 배치
cols = st.columns(4)

for i, m in enumerate(members):
    with cols[i]:
        st.markdown(f"""
            <div style="border: 5px solid lime; padding: 15px; background: rgba(0,0,0,0.8); color: white; border-radius: 15px;">
                <h3>{m['name']}</h3>
                <p><b>별명:</b> {m['nick']}<br><b>MBTI:</b> {m['mbti']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"🔥 {m['name']} 조롱"):
            st.warning(f"🚨 {m['msg']}")
            st.write("**조롱하려면 입금하세요 (복사하기)**")
            st.code(m['bank']) # 클릭하면 바로 복사 가능
            st.button(f"💸 {m['name']}에게 입금 완료!")

st.write("---")

# 6. 샤갈 & 두쫀쿠 광란의 사운드 보드 (텍스트판)
st.header("🔊 무지성 추임새 버튼")
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("샤갈~!"):
        st.markdown("## 🌊 샤갈~!!!!!")
        st.snow()
with c2:
    if st.button("두쫀쿠!!"):
        st.markdown("## 🍪 두! 쫀! 쿠!!")
        st.toast("두툼 쫀득 쿠키 먹고싶다")
with c3:
    if st.button("리으을~?"):
        st.markdown("## 🤪 리으으을~~?")
with c4:
    if st.button("누구라예?"):
        st.markdown("## 🧐 누구라예?!?!")
with c5:
    if st.button("뒷태 브이"):
        st.markdown("## ✌️ (뒤돌음)")

# 7. 마지막 무리수 아이디어: 샤갈 도배기
st.write("---")
st.subheader("🚀 샤갈~! 무한 도배 시스템")
if st.button("샤갈~! 10연타 발사"):
    for _ in range(10):
        st.write("샤갈~! 샤갈~! 샤갈~! 샤갈~! 샤갈~!")
        time.sleep(0.05)
    st.success("샤갈 도배 완료. 이제 좀 조용히 하세요.")

if st.button("🚨 절대 누르지 마시오 (현생 복귀)"):
    st.error("현생 복귀 실패! 평생 경주월드 거지로 사세요!")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ4ZzRyeGZ4ZzRyeGZ4ZzRyeGZ4ZzRyeGZ4ZzRyeGZ4ZzR5JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCheck&rid=giphy.gif&ct=g")