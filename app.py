import pandas as pd
import yfinance as yf
import streamlit as st

share = st.text_input("Input share to check", "GOOG")

data = yf.download(share,start="2021-10-01",end="2021-10-10")

st.pyplot(data.Open-data.Close)

data

