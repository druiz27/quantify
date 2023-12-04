import streamlit as st
from datetime import date

import yfinance as yf

from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objects as go

START_DATE = '2014-01-01'
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Forecasting")

stocks = ("AAPL", "GOOG", "IBM", "AMZN", "MSFT")
selected_stocks = st.selectbox("Select dataset for prediction", stocks)

n_years = st.slider("Years of prediction:", 1, 10)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START_DATE, TODAY)
    data.reset_index(inplace=True)
    return data
data_load_state = st.text("Loading Data....")
data = load_data(selected_stocks)
data_load_state.text("Loading Data....done!")

st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Close'))
    fig.layout.update(title_text='Time Series Data', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_raw_data()

df_training = data[['Date', 'Close']]
df_training = df_training.rename(columns={"Date": "ds", "Close": "y"})

model = Prophet()
model.fit(df_training)
future = model.make_future_dataframe(periods=period)
forecast = model.predict(future)

st.subheader('Forecast Data')
st.write(forecast.tail())

st.write('Forecast')
fig1 = plot_plotly(model, forecast)
st.plotly_chart(fig1)

st.write('Forecast Components')
fig2 = model.plot_components(forecast)
st.write()
