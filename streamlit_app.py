import streamlit as st

# 1. 화면 구성
st.title("☕ 학교 카페 키오스크")
menus = ["아메리카노", "카페라떼", "딸기스무디"]
prices = [3000, 3500, 4500]

# 2. 리스트와 입력 제어 (스트림릿 방식)
selected = st.selectbox("메뉴를 선택하세요", menus)
count = st.number_input("수량", min_value=1, value=1)

if st.button("장바구니 담기"):
    # 리스트에 저장하거나 즉시 계산
    st.write(f"결제 금액: {prices[menus.index(selected)] * count}원")