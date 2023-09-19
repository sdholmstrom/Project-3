from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
st.set_page_config(page_title="Project 3", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

Lottie_coding = load_lottieurl("https://lottie.host/731e06ec-f3f5-4935-937c-a8e89eb5b2c1/TC24OesIGT.json")


# ---- HEADER SECTION ----
st.subheader("Welcome to Project TradeSmart Analyzer :wave:")

st.sidebar.write("""
This website is for informational purposes only. It is not a financial advisor and does not provide financial advice.

You should always do your own research before making any investment decisions.

The information on this website is not guaranteed to be accurate or complete.

By using this website, you agree to the terms and conditions.
""")

#Initial UI
ticker = st.text_input('Ticker', "TSLA").upper()
buttonClicked = st.button('Set')

#Callbacks
if buttonClicked:
  requestString = f"""https://query1.finance.yahoo.com/v10/...{ticker}?modules=assetProfile%2Cprice"""
  request = requests.get(f"{requestString}", headers={"USER-AGENT": "Mozilla/5.0"})
  json = request.json()
  data = json["quoteSummary"]["result"][0]

  st.header("Profile")

  st.metric("sector", data["assetProfile"]["sector"])
  st.metric("industry", data["assetProfile"]["industry"])
  st.metric("website", data["assetProfile"]["website"])
  st.metric("marketCap", data["price"]["marketCap"]["fmt"])

  with st.expander("About Company"):
    st.write(data["assetProfile"]["longBusinessSummary"])

st_lottie(Lottie_coding, height=300, key="coding")

