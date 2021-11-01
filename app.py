import pandas as pd
import yfinance as yf
import streamlit as st
import datetime
import numpy as np
import pydeck as pdk

#c = st.container()

st.title('Online stock checker for Leo')

df = pd.read_csv("nasdaq100.csv")
share_sym = df.symbol.tolist()
share_sym.append('TSLA')
share_sym.sort()

#share = st.text_input("Input share to check", "GOOG")
share = st.selectbox("Input share to check", share_sym)
#date_start = st.date_input("start date","2010-01-01")
date_start = st.date_input("start date",datetime.date(2010,1,1))
date_end = st.date_input('end date')

data = yf.download(share,start=date_start,end=date_end)

#clicked = st.button("Click me")
st.area_chart(data.Open)

st.write("Showing share data for",share,"between",\
         str(date_start),"and",str(date_end))

st.write("And now trying out Pydeck below from example")

df = pd.DataFrame(
         np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
         columns=['lat', 'lon'])

deck = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(latitude=37.76,longitude=-122.4,zoom=11,pitch=50))
                
lys=[pdk.Layer('HexagonLayer',data=df,get_position='[lon, lat]',radius=200,elevation_scale=4,elevation_range=[0, 1000],pickable=True,extruded=True),
        pdk.Layer('ScatterplotLayer',data=df,get_position='[lon, lat]',get_color='[200, 30, 0, 160]',get_radius=200)]
                
st.pydeck_chart(deck,lys)
