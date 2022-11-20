import yfinance as yf

class Stock:
  def __init__(self, ticker):
    self.ticker = ticker 

  def get_company_info(self, ticker):
    return {
      "symbol": yf.Ticker(ticker).info['symbol'],
      "price": yf.Ticker(ticker).info['currentPrice'],
      "volume": yf.Ticker(ticker).info['volume24Hr'],
    }
 
    
