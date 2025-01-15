# Stock Analysis Tool

A Python-based tool for analyzing stock data, calculating metrics, and visualizing stock performance using `yfinance`, `NumPy`, and `Matplotlib`.

## Features
- Fetch historical stock data using `yfinance`.
- Calculate daily returns, average returns, and volatility.
- Generate short-term and long-term moving averages.
- Identify days with the highest and lowest returns.
- Visualize stock closing prices, moving averages, and daily returns.

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - `yfinance`
  - `numpy`
  - `matplotlib`

## Usage
1. Open `stock.py` and update the `ticker` variable with the desired stock symbol (e.g., `GOOG` for Google).
2. Run the script:
   ```bash
   python3 stock.py
   ```
3. The tool will fetch stock data, perform analysis, and generate visualizations.

## Output
- **Console Output**: Key metrics like highest return day, lowest return day, average daily return, and volatility.
- **Visualizations**:
  - Stock closing prices and moving averages.
  - Histogram of daily returns.
  - Scatter plot of daily returns vs. closing prices.

## Example
Run the script for Google stock (`GOOG`), and you'll see:
- Console output with metrics.
- Graphs displaying stock trends and return distributions.
