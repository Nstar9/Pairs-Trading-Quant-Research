import pandas as pd
import itertools
from statsmodels.tsa.stattools import coint

# Alright, loading the stock data that I fetched earlier 👇
data_path = "../data/tech_stocks_data.csv"
print("📥 Loading stock data from CSV...")

df = pd.read_csv(data_path, index_col=0, parse_dates=True)

# Keeping only numeric price columns — don’t want any junk columns here
df = df.select_dtypes(include=['float64', 'int64'])

# Okay, creating all possible stock pairs for testing
stock_pairs = list(itertools.combinations(df.columns, 2))

# Storing the cointegrated pairs if I find any
cointegrated_pairs = []

print("🔎 Running cointegration tests on all pairs... This might take a while 😅")

for stock1, stock2 in stock_pairs:
    try:
        score, p_value, _ = coint(df[stock1], df[stock2])
        print(f"Testing Pair {stock1} - {stock2} | p-value: {p_value:.4f}")
        
        if p_value < 0.1:  # ✅ Relaxed threshold
            print(f"✅ Cointegrated: {stock1} & {stock2} (p-value: {p_value:.4f})")
            cointegrated_pairs.append((stock1, stock2, p_value))
    
    except Exception as e:
        print(f"❌ Error testing {stock1} & {stock2}: {e}")

# Finally, saving the results if I found any good pairs
if cointegrated_pairs:
    result_df = pd.DataFrame(cointegrated_pairs, columns=["Stock 1", "Stock 2", "P-Value"])
    result_df.sort_values("P-Value", inplace=True)
    result_df.to_csv("../data/cointegrated_pairs.csv", index=False)
    print("📄 Cointegration results saved at '../data/cointegrated_pairs.csv'")
else:
    print("❌ No cointegrated pairs found. Might need to try with other stocks or change the timeframe.")

print("✅ Cointegration analysis complete!")








import matplotlib.pyplot as plt
import os

# ✅ Create 'images' folder if not exists
images_dir = "../images"
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print(f"📁 Created directory: {images_dir}")

if cointegrated_pairs:
    # 📈 Pick the first cointegrated pair to visualize
    best_pair = cointegrated_pairs[0]
    stock1, stock2, p_val = best_pair

    # ✅ Calculate the spread
    spread = df[stock1] - df[stock2]

    # ✅ Plotting the spread
    plt.figure(figsize=(12, 6))
    plt.plot(spread, label=f'Spread ({stock1} - {stock2})', color='blue')
    plt.axhline(spread.mean(), color='red', linestyle='--', label='Mean Spread')
    plt.legend()
    plt.title(f"Spread Plot of {stock1} & {stock2}\n(p-value: {round(p_val, 4)})")
    plt.xlabel("Date")
    plt.ylabel("Spread Value")

    # ✅ Save the plot
    plot_path = os.path.join(images_dir, 'spread_plot.png')
    plt.savefig(plot_path)
    plt.close()

    print(f"✅ Spread plot saved at: {plot_path}")
else:
    print("❌ No cointegrated pairs found to plot. Try different stocks or timeframe.")
