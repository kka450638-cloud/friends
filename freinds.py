import streamlit as st
import random
import time

# 1. 페이지 설정: 최대한 무근본하고 시끄럽게!
st.set_page_config(page_title="🎢경주월드: 샤갈&두쫀쿠🎢", layout="wide")

# 2. 광기의 CSS: 배경 깜빡임, 제목 흔들기, 조잡한 버튼 스타일
st.markdown("""
    <style>
    @keyframes blink {
        0% { background-color: #ff00ff; }
        33% { background-color: #00ffff; }
        66% { background-color: #ffff00; }
        100% { background-color: #ff00ff; }
    }
    .stApp {
        animation: blink 0.3s infinite; /* 광속 깜빡이 */
        opacity: 0.85;
    }
    .shaking-title {
        font-size: 80px !important;
        font-weight: 900;
        color: white !important;
        text-shadow: 5px 5px #ff0000, -5px -5px #0000ff;
        text-align: center;
        animation: shake 0.1s infinite;
    }
    @keyframes shake {
        0% { transform: translate(2px, 2px) rotate(0deg); }
        50% { transform: translate(-2px, -3px) rotate(-1deg); }
        100% { transform: translate(2px, 2px) rotate(0deg); }
    }
    .stButton>button {
        width: 100%;
        height: 80px;
        background-color: black !important;
        color: #00ff00 !important;
        border: 5px dashed #ff00ff !important;
        font-size: 22px !important;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.2) rotate(-5deg);
        background-color: white !important;
        color: red !important;
    }
    marquee {
        font-size: 35px;
        color: #000;
        background: #fff;
        font-weight: bold;
        border: 3px solid black;
    }
    .user-card {
        border: 8px double white;
        padding: 15px;
        background: rgba(0,0,0,0.8);
        color: white;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 상단 텍스트 테러 (Marquee)
st.markdown("<marquee>🌊 샤갈~! 샤갈~! 🍪 두쫀쿠!! 두쫀쿠!! 🧐 누구라예?? 🤪 리으을~~?? ✌️ 뒷태 브이!! 👵 할매조끼 입어라!!</marquee>", unsafe_allow_html=True)
st.markdown('<h1 class="shaking-title">🎢경주월드🎢</h1>', unsafe_allow_html=True)

# 4. 사이드바: 거지 수용소 (이미지 링크 수정 완료)
with st.sidebar:
    st.title("💸 거지 수용소")
    # 안정적인 GIPHY 직접 링크로 교체
    st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHRneGZ4ZzRyeGZ4ZzRyeGZ4ZzRyeGZ4ZzRyeGZ4ZzRyeGZ4ZzR5JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCheck/3o7TKMGpx6v2G1ADqE/giphy.gif")
    
    if st.button("내 거지 지수 측정"):
        st.error(f"축하합니다! 당신의 거지 지수는 {random.randint(95, 100)}% 입니다!")
        st.balloons()
    
    st.write("---")
    st.subheader("👵 할매조끼 대여소")
    if st.button("오늘의 조끼 뽑기"):
        vests = ['화려한 빨간 꽃무빔', '칙칙한 갈색 체크', '겨자색 누빔', '보라색 정체불명 조끼']
        st.info(f"선택된 조끼: {random.choice(vests)}")
        st.write("샤갈~하게 잘 어울리네요!")

# 5. 메인 레이아웃: 멤버별 조롱 & 입금 시스템
st.markdown("## 🤡 조롱하려면 입금하세요 (샤갈~!)")

# 멤버 데이터 정의
members = [
    {"name": "이수민", "mbti": "ISFJ", "nick": "남한길", "bank": "카카오뱅크 3333-13-2239193", "msg": "남한길처럼 길 잃기 전에 입금해라 샤갈~!"},
    {"name": "김경아", "mbti": "ENTP", "nick": "발렛파킹", "bank": "카카오뱅크 3333-12-1244746", "msg": "발렛비 입금 안 하면 차 견인한다 두쫀쿠!!"},
    {"name": "강서현", "mbti": "ISFP", "nick": "캉다시마", "bank": "카카오뱅크 3333-15-6915803", "msg": "다시마처럼 끈적하게 조롱받을 준비 됐니?"},
    {"name": "윤혜빈", "mbti": "ESFP", "nick": "수진이", "bank": "카카오페이 010-8789-4037", "msg": "수진아!! 입금 확인 안 되면 조롱 금지다 샤갈~!"}
]

cols = st.columns(4)

for i, m in enumerate(members):
    with cols[i]:
        st.markdown(f"""
            <div class="user-card">
                <h3>{m['name']}</h3>
                <p>({m['mbti']} / {m['nick']})</p>
            </div>
        """, unsafe_allow_html=True)
        
        # 조롱 버튼
        if st.button(f"🔥 {m['name']} 조롱하기"):
            st.warning(f"🚨 {m['msg']}")
            st.write("**조롱하려면 입금하세요(복사하기)**")
            st.code(m['bank']) # 클릭 시 복사 가능하도록 코드 블록 사용
            st.snow()

st.write("---")

# 6. 무지성 추임새 사운드 보드 (텍스트 & 효과)
st.header("🔊 경주월드 공식 추임새 발사기")
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("샤갈~!"):
        st.markdown("# 🌊 샤! 갈~!")
        st.toast("샤갈~! 샤갈~!")
with c2:
    if st.button("두쫀쿠!!"):
        st.markdown("# 🍪 두! 쫀! 쿠!!")
        st.toast("두툼 쫀득 쿠키!!")
with c3:
    if st.button("리으을~?"):
        st.markdown("# 🤪 리으으으으을~~?")
with c4:
    if st.button("누구라예?"):
        st.markdown("# 🧐 누구라예?!?!")
with c5:
    if st.button("뒷태 브이"):
        st.markdown("# ✌️ (뒤돌음)")

# 7. 샤갈 무한 도배 & 현생 찌들기 구역
st.write("---")
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("🚀 샤갈~! 10연타 발사기")
    if st.button("샤갈 도배 시작"):
        for _ in range(10):
            st.write("🌊 샤갈~! 샤갈~! 샤갈~! 샤갈~!")
            time.sleep(0.05)

with col_r:
    st.subheader("😫 현생 찌들기 측정기")
    stress = st.slider("오늘 얼마나 찌들었나요?", 0, 100, 100)
    if stress > 50:
        st.write("### 입금하고 조롱하며 푸세요!!!")

# 8. 바닥 (폭발적인 마무리)
if st.button("🚨 절대 누르지 마시오"):
    st.error("입금해!!! 입금해!!! 입금해!!! 샤갈~!!!")
    st.write("# 💥 두 쫀 쿠 💥")
    st.snow()
    st.balloons()