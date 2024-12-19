from MainClass import PolygonData
import matplotlib.pyplot as plt

class ChildChart(PolygonData):
    def __init__(self):
        super().__init__()  

    def plot_price(self, df):
        if df.empty:
            print("The DataFrame is empty.")
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

chart = ChildChart()

df = chart.get_data(
    ticker="AAPL",  
    multiplier=1,
    timespan="day",
    start_date="2024-01-01",
    end_date="2024-01-10"
)

print("Fetched Data:")
print(df)

chart.plot_price(df)