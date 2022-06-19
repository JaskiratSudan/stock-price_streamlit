import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App.
""")

company_name = st.text_input("Enter Company name")
st.write("**You Selected:** ", company_name)

time_period = st.text_input("Enter Time Period")

st.write('## Showing', time_period, 'year Close Price for ', company_name)

company_data = yf.Ticker(company_name)

company_df = company_data.history(period=time_period+"y")

st.line_chart(company_df.Close)