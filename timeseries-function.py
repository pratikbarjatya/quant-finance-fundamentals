
import yfinance as yf
from datetime import datetime

tickerSymbol = input("Ticker Symbol: ").strip()

ticker = yf.Ticker(tickerSymbol)
stockPrice = ticker.history(period="1d")['Close'].iloc[-1]
print(f"Current Stock Price: {stockPrice}")

print(f"View Historical Information for the Current Stock {tickerSymbol}:")
sy, sm, sd = map(int, input("input start date as yyyy,m,d: ").split(','))
ey, em, ed = map(int, input("input end date as yyyy,m,d: ").split(','))

start = datetime(sy, sm, sd)
end = datetime(ey, em, ed)

historicalPrices = ticker.history(start=start, end=end)

if historicalPrices.empty:
	print("No historical data found for the given date range.")
else:
	# Remove timezone info from index
	historicalPrices.index = historicalPrices.index.tz_localize(None)
	startingDate = start.strftime('%Y%m%d')
	endingDate = end.strftime('%Y%m%d')
	import os
	downloads_folder = os.path.expanduser('./downloads')
	fileName = f"HistoricalStockPrices_{tickerSymbol}_From_{startingDate}_To_{endingDate}.xlsx"
	filePath = os.path.join(downloads_folder, fileName)
	historicalPrices.to_excel(filePath)
	print(f"Historical data saved to {filePath}")
