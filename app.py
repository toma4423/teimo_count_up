import streamlit as st

# ページの設定
st.set_page_config(page_title="てぃもさん用カウントアップ", page_icon="🔢")

# セッション状態の初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

# タイトルの表示
st.title("てぃもさん用カウントアップ")

# 10個でリセットされるウサギの表示
# 10個溜まった瞬間に表示をリセットするため、余りを計算
display_rabbits_count = st.session_state.count % 10
rabbits = "🐇" * max(0, display_rabbits_count)

if rabbits:
    st.write(rabbits)
elif st.session_state.count > 0 and display_rabbits_count == 0:
    st.write("(ウサギが10個溜まってリセットされました！)")
else:
    st.write("(ウサギはいません)")

# カウントアップ関数の定義
def increment_counter():
    st.session_state.count += 1

# カウントダウン関数の定義
def decrement_counter():
    st.session_state.count -= 1

# 数値入力の更新
def update_count():
    st.session_state.count = st.session_state.input_val

# 中央にカウントを表示
st.write("---")
st.markdown(f"<h2 style='text-align: center;'>現在のカウント</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{st.session_state.count}</h1>", unsafe_allow_html=True)

# 数値の直接入力
st.number_input("数値を直接入力", value=st.session_state.count, key="input_val", on_change=update_count)

# ボタンの配置
col1, col2 = st.columns(2)
with col1:
    st.button("カウントアップ", on_click=increment_counter, use_container_width=True)
with col2:
    st.button("カウントダウン", on_click=decrement_counter, use_container_width=True)

st.write("---")

# 雪うさぎのカウント（10個につき1増加）
snow_rabbit_count = max(0, st.session_state.count // 10)
st.write(f"雪うさぎ {snow_rabbit_count}個")
