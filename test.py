from StockData import StockData

a = StockData('ABC.ax')
a.get_market_data('1y','1d')
# attributes = dir(a.stockInfo)
# print(attributes)

print('---Info---')
a.stockInfo.get_analysis
print(a.stockInfo.analysis)

# print('---Recommendations Summary---')
# print(a.stockInfo.revenue_forecasts)


# print('---Financials---')
# print(a.stockInfo.financials)
# print('---Balance sheet---')
# print(a.stockInfo.balance_sheet)
# print('---Cash Flow---')
# print(a.stockInfo.cashflow)
# print('---Earnings---')
# print(a.stockInfo.earnings)
# print('---Sustainability---')
# print(a.stockInfo.sustainability)
# print('---Recomendations---')
# print(a.stockInfo.recommendations)

