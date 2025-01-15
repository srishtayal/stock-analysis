import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'MSFT'
data = yf.download(ticker, start='2018-01-01', end='2020-01-01', group_by='ticker')

if data.empty:
    print("No data fetched. Please check the ticker symbol or date range.")
    exit()

print("Available columns:", data.columns)

try:
    closing_prices = data[('MSFT', 'Close')].values
except KeyError:
    print("'Close' column for ticker MSFT is missing.")
    exit()

data = data.dropna(subset=[('MSFT', 'Close')])

closing_prices = data[('MSFT', 'Close')].values

daily_returns = np.diff(closing_prices) / closing_prices[:-1] * 100
daily_returns = np.insert(daily_returns, 0, 0)

short_term_window = 20
long_term_window = 50

short_term_moving_average = np.convolve(closing_prices, np.ones(short_term_window), 'valid') / short_term_window
long_term_moving_average = np.convolve(closing_prices, np.ones(long_term_window), 'valid') / long_term_window

highest_return_day = np.argmax(daily_returns)
lowest_return_day = np.argmin(daily_returns)

average_daily_return = np.mean(daily_returns)
volatility = np.std(daily_returns)

print(f'Highest return day: {highest_return_day}')
print(f'Lowest return day: {lowest_return_day}')
print(f'Average daily return: {average_daily_return}')
print(f'Volatility: {volatility}')

plt.figure(figsize=(14, 7))

plt.plot(closing_prices, label=f'{ticker} Closing Prices', color='blue')

plt.plot(short_term_moving_average, label=f'{short_term_window}-Day Moving Average', color='orange')
plt.plot(long_term_moving_average, label=f'{long_term_window}-Day Moving Average', color='green')

plt.title(f'{ticker} Stock Analysis', fontsize=16)
plt.xlabel('Days', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(daily_returns, bins=30, color='purple', edgecolor='black', alpha=0.7)
plt.title(f'{ticker} Daily Returns for {ticker}', fontsize=16)
plt.xlabel('Daily Return (%)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(daily_returns[1:], closing_prices[:-1], color='red', alpha=0.6)
plt.title(f'{ticker} Daily Returns vs. Closing Prices', fontsize=16)
plt.xlabel('Daily Return (%)', fontsize=12)
plt.ylabel('Closing Price', fontsize=12)
plt.grid(True)
plt.show()