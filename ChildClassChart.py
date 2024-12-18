from MainClass import PolygonData
polygon = PolygonData()

df = polygon.get_data(
    ticker="TSLA", 
    multiplier=1,  
    timespan="day", 
    start_date="2024-12-10",
    end_date="2024-12-16"   
)

print("Fetched Data:")
print(df)

print("Plotting the price trend...")
polygon.plot_price_trend(df)