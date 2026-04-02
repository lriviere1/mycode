import yfinance as yf
import matplotlib.pyplot as plt

def main():
    # Download META stock data (last 1 month)
    ticker = "META"
    data = yf.download(ticker, period="1mo", interval="1d")

    # Check if data loaded
    if data.empty:
        print("Error: No data found.")
        return

    # Extract closing prices
    dates = data.index
    prices = data["Close"]

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices)

    # Labels and title
    plt.title("Meta (META) Stock Price - Last 1 Month")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")

    # Grid
    plt.grid()

    # Save the graph
    file_name = "meta_stock_last_month.png"
    plt.savefig(file_name)

    print(f"Graph saved as {file_name}")

    # Show the graph
    plt.show()

# Run program
main()