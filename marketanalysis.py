# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 19:01:33 2025

@author: MOHAMMAD FARAZ
"""



import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


data = yf.download("RELIANCE.NS", period="1y")


data["SMA50"] = data["Close"].rolling(50).mean()
data["Returns"] = data["Close"].pct_change()


plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Price")
plt.plot(data["SMA50"], label="50-Day SMA")
plt.title("Reliance - Price & 50-Day SMA")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.savefig("reliance_price_sma.png", dpi=300)
plt.show()


plt.figure(figsize=(8,5))
plt.hist(data["Returns"].dropna(), bins=40)
plt.title("Daily Returns Distribution - Reliance")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("reliance_returns_hist.png", dpi=300)
plt.show()
