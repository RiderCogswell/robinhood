import yfinance as yf

def get_company_info(self, ticker):
  return yf.Ticker(ticker).info
