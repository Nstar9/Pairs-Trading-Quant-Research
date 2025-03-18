import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the dataset
data_path = "../data/tech_stocks_data.csv"
df = pd.read_csv(data_path, index_col=0, parse_dates=True)

# 🔎 Check what columns you got
print("Columns in CSV:", df.columns)

# Example if you want to rename columns manually (Optional based on what you see)
# df.columns = ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'TSLA']  # Replace as needed

# 🔥 Pick the correct columns based on what you see
stock1_col = df.columns[0]  # or manually set to 'Close' or 'Close.1'
stock2_col = df.columns[1]

print(f"✅ Running backtest on: {stock1_col} & {stock2_col}")




df[stock1_col] = pd.to_numeric(df[stock1_col], errors='coerce')
df[stock2_col] = pd.to_numeric(df[stock2_col], errors='coerce')


# Calculate spread
spread = df[stock1_col] - df[stock2_col]
spread_mean = spread.mean()
spread_std = spread.std()

# Define thresholds
entry_threshold = 1 * spread_std
exit_threshold = 0

# Backtest logic
position = 0
pnl = []
spread_series = []

for i in range(len(spread)):
    current_spread = spread.iloc[i]
    spread_series.append(current_spread)

    # Entry logic
    if position == 0:
        if current_spread > spread_mean + entry_threshold:
            position = -1
            entry_price = current_spread
            print(f"🚀 SHORT at {df.index[i]} Spread: {current_spread:.2f}")
        elif current_spread < spread_mean - entry_threshold:
            position = 1
            entry_price = current_spread
            print(f"🚀 LONG at {df.index[i]} Spread: {current_spread:.2f}")

    # Exit logic
    elif position != 0:
        if abs(current_spread - spread_mean) < exit_threshold:
            profit = (entry_price - current_spread) * position
            pnl.append(profit)
            print(f"💰 EXIT at {df.index[i]} | Profit: {profit:.2f}")
            position = 0

total_pnl = sum(pnl)
print(f"\n✅ Backtest done! Total PnL: {total_pnl:.2f}")

# Plotting the spread
plt.figure(figsize=(12, 6))
plt.plot(spread_series, label='Spread')
plt.axhline(spread_mean, color='red', linestyle='--', label='Mean')
plt.title(f"Spread Backtest - {stock1_col} & {stock2_col}")
plt.legend()

# ✅ Create images directory if not exists
os.makedirs("../images", exist_ok=True)

# ✅ Save plot with absolute path for confirmation
# Get the base directory of your project (Pairs-Trading-Quant-Research)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Make sure images folder exists inside your project
images_dir = os.path.join(base_dir, "images")
os.makedirs(images_dir, exist_ok=True)

# Set the full path for saving
full_path = os.path.join(images_dir, "backtest_spread_plot.png")
plt.savefig(full_path)
plt.close()

print(f"✅ Backtest plot saved at: {full_path}")
