import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
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
    def plot_price_trend(self, df):

        if df.empty:
            print("Data not available to plot.")
        else:
            plt.figure(figsize=(10, 6))
            plt.plot(df['Date'], df['Close'], label='Close Price', marker='o')
            plt.title(f"Price Trend for Stock")
            plt.xlabel("Date")
            plt.ylabel("Close Price")
            plt.legend()
            plt.grid()
            plt.show()
    def save_to_sqlite(df, database_name, table_name):
        conn = sqlite3.connect(database_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data saved into a table '{table_name}' in database '{database_name}'.")

    def query_sqlite(database_name, query):
        conn = sqlite3.connect(database_name)
        result = pd.read_sql_query(query, conn)
        conn.close()
        return result