import pandas as pd
import yfinance as yf
import streamlit as st

#c = st.container()

st.title('Online stock checker for Leo')

df = pd.read_csv("nasdaq100.csv")
share_sym = df.symbol.tolist()
share_sym.append('TSLA')
share_sym.sort()

#share = st.text_input("Input share to check", "GOOG")
share = st.selectbox("Input share to check", share_sym)
date_start = st.date_input('start date',value='01-01-2010')
date_end = st.date_input('end date')

data = yf.download(share,start=date_start,end=date_end)

#clicked = st.button("Click me")
st.area_chart(data.Open)

st.write("Showing share data for",share,"between",\
         str(date_start),"and",str(date_end))

