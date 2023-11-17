import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_tickers():
    tickers = input("Enter the stock tickers separated by a comma (e.g., AAPL, MSFT, AMZN): ").split(',')
    return [ticker.strip().upper() for ticker in tickers]

def get_balancing_coefficients(tickers):
    coefficients = []
    for ticker in tickers:
        coefficient = float(input(f"Enter balancing coefficient for {ticker}: "))
        coefficients.append(coefficient)
    return coefficients

def fetch_data(tickers):
    data = yf.download(tickers, start="2022-01-01", end="2023-01-01")['Close']
    return data

def calculate_total_return(data, coefficients):
    normalized_data = data / data.iloc[0]
    portfolio = normalized_data.dot(coefficients)
    total_return = (portfolio.iloc[-1] - 1) * 100
    return portfolio, total_return  # Return both the portfolio data and the total return

def plot_data(data, portfolio):
    plt.figure(figsize=(12, 6))

    # Plot each asset
    for column in data.columns:
        plt.plot(data.index, data[column] / data[column].iloc[0], label=column)

    # Plot combined portfolio
    plt.plot(portfolio.index, portfolio, label="Combined Portfolio", linewidth=2, linestyle='--')

    plt.title("Asset Prices and Combined Portfolio Return")
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.legend()
    plt.grid(True)
    plt.show()

tickers = get_tickers()
coefficients = get_balancing_coefficients(tickers)

data = fetch_data(tickers)
portfolio, total_return = calculate_total_return(data, coefficients)

plot_data(data, portfolio)

print(f"The total return of your ETF is {total_return:.2f}%")