from MainClass import PolygonData
polygon = PolygonData()

df = polygon.get_data(
    ticker="TSLA", 
    multiplier=1, 
    timespan="day", 
    start_date="2024-01-01", 
    end_date="2024-01-10"
)
print("Fetched Data:")
print(df)

print("Plotting the price trend.")
polygon.plot_price_trend(df)

database_name = "stocks.db"
table_name = "tesla_data"
polygon.save_to_sqlite(df, database_name, table_name)

print("Query Results:")
query_result = polygon.query_sqlite(
    database_name=database_name,
    query="SELECT Date, Close FROM tesla_data WHERE Close > 250 ORDER BY Date ASC"
)
print(query_result)
