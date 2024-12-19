import matplotlib.pyplot as plt
from MainClass import PolygonData

class ChartsPolygonData(PolygonData):
    def __init__(self):
        super().__init__()

    def plot_stock_prices(self, ticker, multiplier, timespan, start_date, end_date):
        stock_data = self.get_data(ticker, multiplier, timespan, start_date, end_date)

        if stock_data.empty:
            print("No data retrieved.")
            return

        stock_data.plot(x="Date", y="Close", title=f"{ticker} Stock Prices", xlabel="Date", ylabel="Close Price (USD)")
        plt.show()

polygon_data = ChartsPolygonData()
polygon_data.plot_stock_prices(
    ticker="AAPL", 
    multiplier=1, 
    timespan="day", 
    start_date="2024-12-10", 
    end_date="2024-12-16"
)

