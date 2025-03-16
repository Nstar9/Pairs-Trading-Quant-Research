import yfinance as yf
import pandas as pd
import os

# Alright, let’s grab historical stock data for 20 top tech companies in the S&P 500.
# We’ll analyze their prices for the past 5 years.

tech_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "NFLX",
               "ADBE", "CRM", "INTC", "AMD", "QCOM", "CSCO", "ORCL", "IBM",
               "PYPL", "UBER", "SNAP", "SHOP"]

# Looking at data from March 16, 2019, to today. A good 5-year range to analyze trends.
start_date = "2019-03-16"
end_date = "2025-03-13"

print("Fetching stock data... This might take a few seconds.")

# Pull adjusted closing prices for all stocks
df = yf.download(tech_stocks, start=start_date, end=end_date)
print(df.columns)  # Debug: Check available column names

# Ensure we're selecting the right column
if "Adj Close" in df.columns:
    df = df["Adj Close"]
elif "Close" in df.columns:
    df = df["Close"]  # Fallback if 'Adj Close' is unavailable
else:
    raise KeyError("Neither 'Adj Close' nor 'Close' found in data")


# Just making sure there are no missing values. If there are, we’ll drop them.
df.dropna(inplace=True)

# Saving this dataset so I don’t have to keep pulling from Yahoo Finance every time.
csv_path = "../data/tech_stocks_data.csv"



# Define the directory and file path
data_dir = "../data"
csv_path = os.path.join(data_dir, "tech_stocks_data.csv")

# Ensure the directory exists
if not os.path.exists(data_dir):
    os.makedirs(data_dir)  # Create the directory if it doesn't exist
    print(f"📂 Created directory: {data_dir}")

# Save the dataframe to CSV
df.to_csv(csv_path)

print(f"✅ Done! Stock data saved at: {csv_path}")


