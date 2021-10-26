import pandas as pd
import yfinance as yf
import streamlit as st

user_input = st.text_input("Input share to check", "GOOG")

data = yf.download("GOOG",start="2021-10-01",end="2021-10-10")

data

"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
---
"""

