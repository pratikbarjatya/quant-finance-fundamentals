import pandas as pd

arrayOfSymbols = ["AAPL","FB","GOOG"]
import os

token = os.getenv("IEX_API_TOKEN")
if not token:
    raise ValueError("IEX_API_TOKEN environment variable not set")
historicalStockPrices = pd.DataFrame()

for x in arrayOfSymbols:
    historicalStockPrices[x] = pd.read_json('https://cloud.iexapis.com/stable/stock/'+x+
                                            '/chart/1y?token='+token+'')["close"]   

historicalStockPrices.head(5)
