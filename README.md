

# 📈 Pairs Trading - Quantitative Research Project

## 🔎 Objective
This project implements a **Statistical Arbitrage - Pairs Trading Strategy** analyzing **20 US Tech Stocks** from the **S&P 500**, using **cointegration**, **mean-reversion**, and **backtesting** techniques.

✅ Key steps:
- Fetching historical stock data (2005-2025)
- Testing pairs for cointegration
- Backtesting the strategy
- Generating trading signals
- Visualizing performance

---

## 📅 Dataset Details
- **Stocks:** AAPL, MSFT, GOOG, AMZN, META, NVDA, TSLA, NFLX, CRM, IBM, PYPL, etc.
- **Source:** `yfinance` API
- **Data Range:** 2005 - 2025
- **Frequency:** Daily (Adjusted Close Prices)

---

## ⚙️ Project Pipeline
1. **Data Fetching (`fetch_data.py`)**
   - Pulled tech stock data for 20 years (2005-2025)
   - Saved in `data/tech_stocks_data.csv`

2. **Cointegration Testing (`check_cointegration.py`)**
   - Ran Engle-Granger cointegration tests
   - Filtered pairs with significant p-values (p < 0.05)

3. **Backtesting (`backtest.py`)**
   - Created the spread of cointegrated pairs
   - Checked the spread behavior over time
   - Calculated PnL for basic mean-reversion strategy

4. **Trading Logic (`trading_logic.py`)**
   - Applied 1 standard deviation threshold rules
   - Generated buy/sell signals

5. **Visualization**
   - Plotted spreads and trading signals
   - Saved plots in `images/`

---

## 🗂 Project Structure
``


---

## 📊 Key Learnings
✅ Learned how **cointegration** forms the basis for Pairs Trading  
✅ Understood **mean-reversion** concept and backtesting strategies  
✅ Hands-on **data extraction**, **statistical testing**, and **signal generation**  
✅ Visualized results for better analysis and reporting

---

## 💻 Technologies Used
- Python 3
- Libraries: `pandas`, `numpy`, `matplotlib`, `statsmodels`, `yfinance`
- Jupyter Notebook
- Git / GitHub

---

## 📈 Example Visualizations (Saved in `/images/`)
- Spread plots of pairs over time
- Trading signal plots with entry/exit points

---

## ✅ Next Steps / Improvements
- Test with different sectors (Finance, Energy, Healthcare)
- Explore dynamic hedge ratios (Kalman Filter / PCA)
- Include transaction costs and slippage
- Automate the full pipeline

---

## 📬 Project Info
- **Author:** Niraj Patil
- **Project Duration:** 3-4 Days
- **Timeframe of Data:** 2005 - 2025
- **GitHub Repo:** [Pairs-Trading-Quant-Research](https://github.com/Nstar9/Pairs-Trading-Quant-Research)

---

## ⭐ Conclusion
This project helped me build a strong foundation in **Statistical Arbitrage - Pairs Trading**, covering data handling, cointegration tests, backtesting logic, and visualization. 

It's the **first of 10 Quant Finance projects** on my roadmap to strengthen my Quant profile and secure a role in **top quantitative finance firms**.

