"""Code for collecting data"""

from pathlib import Path
import datetime as dt
import pandas as pd
import yfinance as yf

def get_data(ticker, period):
    """Function to query yfinance for ticker and period"""
    yf_ticker = yf.Ticker(ticker)
    ticker_data = yf_ticker.history(period)
    ticker_data = ticker_data[['Open', 'High', 'Low', 'Close', 'Volume']]
    ticker_data.index = ticker_data.index.tz_localize(None)
    ticker_data['stock_symbol'] = ticker
    return ticker_data

def main():
    """Function to query yfinance for ticker and period"""
    period = '1mo'
    ticker = 'QQQ'
    data = get_data(ticker, period)
    print(data)
    data_dir = 'data'
    csv_path = Path(data_dir, "raw", ticker + ".csv")
    print(csv_path)
    data.to_csv(csv_path)


if __name__ == "__main__":
    main()
