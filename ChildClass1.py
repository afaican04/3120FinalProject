from MainClass import PolygonData

class ChildPolygonData(PolygonData):
    def __init__(self):
        super().__init__()

    def print_data_head(self, ticker, multiplier, timespan, start_date, end_date):
        stock_data = self.get_data(ticker, multiplier, timespan, start_date, end_date)

        if stock_data.empty:
            print("No data retrieved.")
        else:
            print(stock_data.head())
polygon_data = ChildPolygonData()

polygon_data.print_data_head(
    ticker="AAPL", 
    multiplier=1,
    timespan="day",
    start_date="2024-01-01", 
    end_date="2024-01-10"    
)