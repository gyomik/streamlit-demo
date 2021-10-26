import pandas as pd
import yfinance as yf
import streamlit as st

c = st.empty()

share = st.text_input("Input share to check", "GOOG")
date_start = st.date_input('start date')
date_end = st.date_input('end date')

data = yf.download(share,start=date_start,end=date_end)

#clicked = st.button("Click me")
st.area_chart(data.Open)

st.write("Good")
c.write("Showing share data for",share,"between",\
         str(date_start),"and",str(date_end))

