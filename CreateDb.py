from MainClass import PolygonData
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

class ChildPolygonData(PolygonData):
    def __init__(self):
        super().__init__()

    def plot_price_trend(self, df):
        if df.empty:
            print("The DataFrame is empty. Cannot plot.")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(df["Date"], df["Close"], marker="o", label="Close Price")
        plt.title("Stock Price Trend", fontsize=16)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Close Price (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

    def save_to_sqlite(self, df, database_name, table_name):
        if df.empty:
            print("The DataFrame is empty. Nothing to save.")
            return

        connection = sqlite3.connect(database_name)
        df.to_sql(table_name, connection, if_exists="replace", index=False)
        print(f"Data saved to {database_name} in the table {table_name}.")
        connection.close()

    def query_sqlite(self, database_name, query):
        connection = sqlite3.connect(database_name)
        result = pd.read_sql_query(query, connection)
        connection.close()
        return result

polygon_data = ChildPolygonData()

df = polygon_data.get_data(
    ticker="TSLA",  
    multiplier=1,
    timespan="day",
    start_date="2024-01-01",
    end_date="2024-01-10"
)

if df.empty:
    print("No data was fetched.")
else:
    print("Fetched Data:")
    print(df)

    polygon_data.plot_price_trend(df)

    database_name = "stocks.db"
    table_name = "tesla_data"
    polygon_data.save_to_sqlite(df, database_name, table_name)

    query_all = "SELECT * FROM tesla_data"
    all_data = polygon_data.query_sqlite(database_name, query_all)
    print("All Data in Table:")
    print(all_data)

    query = "SELECT Date, Close FROM tesla_data WHERE Close > 250 ORDER BY Date ASC"
    query_result = polygon_data.query_sqlite(database_name, query)
    print("Query Results:")
    print(query_result)