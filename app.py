import pandas as pd
import yfinance as yf

data = yf.download("GOOG",start="2021-10-01",end="2021-10-10")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

data
