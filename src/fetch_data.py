# 📈 Alright, starting fresh - fetching stock data for my Quant Research Project
import yfinance as yf
import pandas as pd
import os

# ✅ Creating the 'data' folder if it doesn't exist - need this to store the CSV
if not os.path.exists("../data"):
    os.makedirs("../data")
    print("✅ 'data' folder created successfully!")

# 📌 List of top tech stocks I want to analyze (Big players from S&P 500)
tech_stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA",
    "NFLX", "ADBE", "CRM", "INTC", "AMD", "QCOM", "CSCO",
    "ORCL", "IBM", "PYPL", "UBER", "SNAP", "SHOP"
]

# 📅 Pulling 6 years of data - decent range for analysis
start_date = "2019-03-16"
end_date = "2025-03-16"

print("📥 Fetching stock data... Might take a sec 🕒")

# 🔄 Downloading data from Yahoo Finance
df = yf.download(tech_stocks, start=start_date, end=end_date)

# ✅ Checking if data came with MultiIndex (sometimes it does)
if isinstance(df.columns, pd.MultiIndex) and 'Adj Close' in df.columns.levels[0]:
    data = df['Adj Close']
    print("✅ Pulled 'Adj Close' prices - this is what really matters for analysis")
else:
    data = df  # fallback if 'Adj Close' isn't available
    print("⚠️ 'Adj Close' not found, using raw data")

# 💾 Saving the data to CSV so I don't have to fetch every time
csv_path = "../data/tech_stocks_data.csv"
data.to_csv(csv_path)
print(f"✅ Data saved successfully at '{csv_path}'")
