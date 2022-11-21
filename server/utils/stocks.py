import yfinance as yf
import requests_cache

class Stock:
  def __init__(self, ticker):
    self.ticker = ticker 

  def get_company_info(self, ticker):
    return [{
      "symbol": yf.Ticker(ticker).info['symbol'],
      "price": yf.Ticker(ticker).info['currentPrice'],
      "volume": yf.Ticker(ticker).info['volume24Hr'],
    }]



session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'
ticker = yf.Ticker('msft aapl goog', session=session)
# The scraped response will be stored in the cache
print(ticker.actions)