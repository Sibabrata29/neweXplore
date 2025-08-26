import os
import time
import requests
import pandas as pd
import streamlit as st
from functools import lru_cache

st.set_page_config(page_title="Encore Streamlit on Render", page_icon="🧩", layout="wide")

# --- Sidebar ---
st.sidebar.title("⚙️ Settings")
st.sidebar.caption("All secrets are read from environment variables on Render.")
api_key = os.getenv("API_KEY", "not-set")
st.sidebar.write("API_KEY:", "✅ set" if api_key != "not-set" else "❌ missing")

timeout = st.sidebar.slider("Request timeout (sec)", 3, 30, 10)

st.sidebar.markdown("---")
st.sidebar.caption("Build: pinned dependencies • reproducible deploys")

# --- Header ---
st.title("🧩 Encore: Streamlit + GitHub + Render")
st.write("Clean UI • Live web access • Secrets in env • Shareable globally.")

# --- Cached data demo ---
@lru_cache(maxsize=32)
def slow_compute(n: int) -> int:
    time.sleep(1)  # simulate heavy work
    return n * n

col1, col2 = st.columns(2)
with col1:
    n = st.number_input("Try cached compute (n²)", min_value=0, max_value=10000, value=42, step=1)
    if st.button("Compute"):
        st.success(f"Result: {slow_compute(int(n))}")

with col2:
    uploaded = st.file_uploader("Optional: upload a CSV to preview")
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df.head(50), use_container_width=True)

# --- Live web access demo (GET) ---
st.subheader("🌐 Live Web Fetch")
url = st.text_input("URL to fetch (GET)", value="https://httpbin.org/get")
if st.button("Fetch"):
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        st.code(resp.text[:2000], language="json")
        st.caption(f"Status {resp.status_code}, {len(resp.text)} bytes")
    except Exception as e:
        st.error(f"Fetch failed: {e}")

# --- Example: using a secret/API key (no real call, just demonstrates env) ---
st.subheader("🔐 Secrets handled via environment")
if api_key == "not-set":
    st.warning("Set API_KEY in Render → Environment → Environment Variables.")
else:
    st.success("API_KEY is available to your code (not printed here).")

st.markdown("---")
st.caption("Deployed on Render • App template © You • Streamlit best practices applied.")