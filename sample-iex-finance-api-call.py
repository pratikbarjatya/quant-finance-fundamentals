import pandas as pd
import os

sym = "AAPL"  # This is not case-sensitive
token = os.environ.get("IEX_API_TOKEN")
if not token:
	raise ValueError("API token not found. Please set the IEX_API_TOKEN environment variable.")
df_temp = pd.read_json('https://cloud.iexapis.com/stable/stock/'+sym+'/chart/1y?token='+token+'')

df_temp.set_index('date',inplace=True)
stock_hist = df_temp['close']
stock_hist.tail(5)
