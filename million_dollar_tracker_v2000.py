
import streamlit as st
import pandas as pd

def run_million_dollar_tracker():
    st.set_page_config(page_title="Million Dollar Tracker", layout="centered")
    st.title("🚀 Million Dollar Tracker")
    st.markdown("رحلتك من **2,000 دولار** إلى **2,000,000 دولار**!")

    if "balance" not in st.session_state:
        st.session_state.balance = 2000.0
    if "trades" not in st.session_state:
        st.session_state.trades = 0
    if "log" not in st.session_state:
        st.session_state.log = []

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📈 الرصيد الحالي", value=f"${st.session_state.balance:,.2f}")
    with col2:
        st.metric(label="🔢 عدد الصفقات", value=st.session_state.trades)

    st.progress(min(st.session_state.balance / 2_000_000, 1.0))

    st.markdown("### ✍️ أدخل نسبة الربح أو الخسارة للصفقة الحالية:")
    trade_result = st.number_input("نسبة الربح/الخسارة (%)", value=10.0, step=0.1)

    if st.button("✅ تسجيل الصفقة"):
        change = st.session_state.balance * (trade_result / 100)
        st.session_state.balance += change
        st.session_state.trades += 1
        st.session_state.log.append({
            "Trade": st.session_state.trades,
            "Result (%)": trade_result,
            "Balance": round(st.session_state.balance, 2)
        })

    if st.button("🔄 إعادة تعيين"):
        st.session_state.balance = 2000.0
        st.session_state.trades = 0
        st.session_state.log = []

    if st.session_state.log:
        st.markdown("### 📜 سجل الصفقات:")
        st.dataframe(pd.DataFrame(st.session_state.log))

run_million_dollar_tracker()
