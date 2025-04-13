import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download crude oil data
df = yf.download("CL=F", start="2020-01-01", end="2024-01-01")
df.dropna(inplace=True)

# Manually calculate RSI
delta = df['Close'].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
df['rsi'] = 100 - (100 / (1 + rs))

# Moving averages
df['ma_short'] = df['Close'].rolling(window=10).mean()
df['ma_long'] = df['Close'].rolling(window=30).mean()

# Signals
df['buy_signal'] = (df['rsi'] < 30) & (df['ma_short'] > df['ma_long']) & (df['ma_short'].shift(1) <= df['ma_long'].shift(1))
df['sell_signal'] = (df['rsi'] > 70) | ((df['ma_short'] < df['ma_long']) & (df['ma_short'].shift(1) >= df['ma_long'].shift(1)))

# Plot
plt.figure(figsize=(15, 8))
plt.plot(df['Close'], label='Crude Oil Price', alpha=0.5)
plt.plot(df['ma_short'], label='10-day MA', linestyle='--')
plt.plot(df['ma_long'], label='30-day MA', linestyle='--')
plt.scatter(df.index[df['buy_signal']], df['Close'][df['buy_signal']], marker='^', color='green', label='Buy Signal', s=100)
plt.scatter(df.index[df['sell_signal']], df['Close'][df['sell_signal']], marker='v', color='red', label='Sell Signal', s=100)
plt.title("Commodity Trading Algorithm - Buy/Sell Signals")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("artemis_signals.png")
plt.show()
