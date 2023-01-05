# Get the stocks history data to CSV file
import yfinance as yf
ticker = 'ORCL'
data = yf.download(tickers=ticker)
data.to_csv(ticker + ".csv")
