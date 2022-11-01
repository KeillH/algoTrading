import yfinance as yf

class StockData:
    """
    The StockData class holds a single stocks historical data
    
    stockInfo: infomation about the stock
    marketData: Various quantitative values of the stock vs time
    stockOpen: Stock dat Open prices.
    stockClose: Stock date Close prices.
    stockHigh: Stock date High prices.
    stockLow: Stock date Low prices
    stockVolume: Stock date Volume.
    """
    
    def __init__(self, ticker):
        self.ticker = ticker
        
        
    def disp_ticker(self):
        #print(self.ticker)
        return self.ticker
    
    def get_market_data(self,
                        period,
                        interval,
                        start=None,
                        end=None):
        """
        Parameters
        ----------
        period : String
            Duration of data obtained.
            Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
        interval : String
            Frequency of stock data.
            Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo.
        start : String, optional
            Start date string (YYYY-MM-DD) or _datetime.
            Default is 1900-01-01.
        end : String, optional
            End date strong (YYYY-MM-DD) or _datetime.
            Default is now.

        Returns
        -------
        None.
        """
        self.period = period
        self.interval = interval
        self.stockInfo = yf.Ticker(self.ticker)
        self.marketData = self.stockInfo.history(period=period,
                                        interval=interval,
                                        start=start,
                                        end=end)
        self.stockOpen = self.marketData['Open']
        self.stockClose = self.marketData['Close']
        self.stockHigh = self.marketData['High']
        self.stockLow = self.marketData['Low']
        self.stockVolume = self.marketData['Volume']