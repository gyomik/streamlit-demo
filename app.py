import pandas as pd
import yfinance as yf
import streamlit as st

share = st.text_input("Input share to check", "GOOG")
date_start = st.date_input('start date')
print(date_start)

data = yf.download(share,start="2021-10-01",end="2021-10-10")

#clicked = st.button("Click me")
st.area_chart(data.Open)

data

