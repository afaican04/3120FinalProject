from MainClass import PolygonData  

ticker = "AAPL"
start_date = "2024-12-10" 
end_date = "2024-12-16"    
multiplier = 1
timespan = "day"

polygon_data = PolygonData()

stock_data = polygon_data.get_data(ticker, multiplier, timespan, start_date, end_date)

if not stock_data.empty:
    print(stock_data.head())
else:
    print("No data retrieved.")
