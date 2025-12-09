# Market Analysis: Reliance Stock Trend & Moving Average Study

This mini-project performs a simple market analysis on **Reliance Industries (RELIANCE.NS)** using Python.  
It highlights price trends, moving averages, and return distribution — demonstrating data-driven thinking and a growing interest in financial markets.

---

##  Objectives

- Download 1-year stock price data using `yfinance`
- Compute the **50-Day Simple Moving Average (SMA50)**
- Visualize price trends and momentum
- Analyze daily returns distribution to understand volatility

---

##  Tools & Libraries Used

- Python  
- yfinance  
- pandas  
- matplotlib  
- Spyder / Anaconda  

---

##  Visualizations Included

### **1. Price vs 50-Day SMA**
Shows the daily closing price of Reliance along with the SMA50 to identify medium-term trend direction.

-> *File:* `reliance_price_sma.png`

---

### **2. Daily Returns Histogram**
Displays the distribution of daily returns over the last year, illustrating volatility patterns.

-> *File:* `reliance_returns_hist.png`

---

##  Key Insights

- Reliance’s price shows a stable upward movement with minor corrections.  
- The **50-day SMA** smoothens short-term fluctuations and reflects trend momentum.  
- Daily returns cluster around zero with occasional spikes, indicating normal volatility for a large-cap stock.  

These indicators help understand price behavior and market sentiment.

---

##  Project Files

| File | Description |
|------|-------------|
| `marketanalysis.py` | Python script for the analysis |
| `reliance_price_sma.png` | Price + 50-Day SMA plot |
| `reliance_returns_hist.png` | Returns histogram |
| `README.md` | Documentation |

---

##  How to Run

1. Install dependencies:
   ```bash
   pip install yfinance pandas matplotlib
   ```
2. Run the analysis:
   ```bash
   python marketanalysis.py
   ```
3. The plots will be saved in the same folder.

---

##  Author

**Mohammad Faraz**  
B.Tech CSE Student  
Python • Data Analysis • Financial Markets (Learning)


