import yfinance as yf

def get_company_info(ticker):
  return {
    "symbol": yf.Ticker(ticker).info['symbol'],
    "price": yf.Ticker(ticker).info['currentPrice'],
    "volume": yf.Ticker(ticker).info['volume24Hr'],
  }

    
