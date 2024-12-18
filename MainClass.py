import requests
import pandas as pd
from key import API_KEY  

class PolygonData:
    def __init__(self):
        self.api_key = API_KEY 
        self.base_url = "https://api.polygon.io/v2/aggs/ticker"
    
    def get_data(self, ticker, multiplier, timespan, start_date, end_date):
        
        url = f"{self.base_url}/{ticker}/range/{multiplier}/{timespan}/{start_date}/{end_date}?apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if "results" in data:
            df = pd.DataFrame(data["results"])
            df['t'] = pd.to_datetime(df['t'], unit='ms')
            df.rename(columns={'t': 'Date', 'o': 'Open', 'h': 'High', 'l': 'Low', 'c': 'Close', 'v': 'Volume'}, inplace=True)
            return df
        else:
            print("Error getting data:", data)
            return pd.DataFrame()  

