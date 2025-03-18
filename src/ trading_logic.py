import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 🔎 Load the spread data (from backtest or cointegration)
spread_data = pd.read_csv('../data/spread_data.csv', parse_dates=True)

# ✅ Define trading thresholds (1 standard deviation)
spread_mean = spread_data['Spread'].mean()
spread_std = spread_data['Spread'].std()
upper_threshold = spread_mean + spread_std
lower_threshold = spread_mean - spread_std

# 💹 Initialize trading signals
spread_data['Signal'] = 0
spread_data.loc[spread_data['Spread'] > upper_threshold, 'Signal'] = -1  # SHORT signal
spread_data.loc[spread_data['Spread'] < lower_threshold, 'Signal'] = 1   # LONG signal

# ✅ Print sample signals
print(spread_data[['Spread', 'Signal']].head())

# 📈 Optional Visualization
plt.figure(figsize=(12, 6))
plt.plot(spread_data['Spread'], label='Spread')
plt.axhline(upper_threshold, color='red', linestyle='--', label='Upper Threshold (Short)')
plt.axhline(lower_threshold, color='green', linestyle='--', label='Lower Threshold (Long)')
plt.legend()
plt.title('Trading Signals on Spread')
plt.xlabel('Time')
plt.ylabel('Spread')

import os
images_dir = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(images_dir, exist_ok=True)

plot_path = os.path.join(images_dir, "trading_signals_plot.png")
plt.savefig(plot_path)
print(f"✅ Trading signals plot saved at {plot_path}")


plt.show()

# ✅ Save signals for backtesting
spread_data.to_csv('../results/trading_signals.csv', index=False)
print("✅ Trading signals saved at '../results/trading_signals.csv'")
