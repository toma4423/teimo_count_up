import streamlit as st

# ページの設定
st.set_page_config(page_title="てぃもさん用カウントアップ", page_icon="🔢")

# タイトルの表示
st.title("てぃもさん用カウントアップ")

# セッション状態の初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

# カウントアップ関数の定義
def increment_counter():
    st.session_state.count += 1

# 中央にカウントを表示するためのスタイル（オプション）
st.write("---")
st.markdown(f"<h2 style='text-align: center;'>現在のカウント</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{st.session_state.count}</h1>", unsafe_allow_html=True)

# ボタンの配置（中央寄せにする工夫）
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("カウントアップ", on_click=increment_counter, use_container_width=True):
        pass

st.write("---")
