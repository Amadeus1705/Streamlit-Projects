import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
# define prev_year in the same format
prev_year = (datetime.today() - pd.DateOffset(years=1)).strftime('%Y-%m-%d')




st.write("""
        # Stock Price App to show past year movement of a stock
        
        
        Shown are the stock closing price and volume of Google
         
         
         """)

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start=prev_year,end=today)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)