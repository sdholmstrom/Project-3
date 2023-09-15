import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
from dotenv import load_dotenv
load_dotenv()

# ---- HEADER SECTION ----
st.subheader("Welcome to Project TradeSmart Analyzer :wave:")

st.sidebar.write("""
Tradesmart Analyser is for informational purposes only. It is not a financial advisor and does not provide financial advice.

You should always do your own research and due dilligance before making any investment decisions.

The information on this website is not guaranteed to be accurate or complete.

By using this website, you agree to the terms and conditions.
""")


#Initial UI
ticker = st.text_input('Ticker', "AAPL").upper()
buttonClicked = st.button('Set')


# To extract and parse fundamental data from finviz website
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# For parsing financial statements data from financialmodelingprep api
from urllib.request import urlopen
import json
def get_jsonparsed_data(url):
    req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}) 
    response = urlopen(req)
    data = response.read().decode("utf-8")
    return json.loads(data)

#financialmodelingprep api url
base_url = "https://financialmodelingprep.com/api/v3/"

# Financial Modeling Prep API demo version only provides AAPL
apiKey = os.getenv('apiKey')
ticker = 'TGT'


q_cash_flow_statement = pd.DataFrame(get_jsonparsed_data(base_url+'cash-flow-statement/' + ticker + '?period=quarter' + '&apikey=' + apiKey))
q_cash_flow_statement = q_cash_flow_statement.set_index('date').iloc[:] # extract for last 4 quarters
q_cash_flow_statement = q_cash_flow_statement.apply(pd.to_numeric, errors='coerce')

q_cash_flow_statement.iloc[::].head()