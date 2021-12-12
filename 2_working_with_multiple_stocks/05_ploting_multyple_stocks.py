import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path to given ticker symbol."""
    return os.path.join(base_dir, f'{symbol}.csv')

def get_data(symbols, dates):
    """Read stock data (Adj Close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(
            symbol_to_path(symbol),
            index_col='Date',
            parse_dates=True,
            usecols=['Date', 'Adj Close'],
            na_values=['nan'],
        )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        df = df.dropna()

    return df

def plot_data(df, title='Stock Prices'):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.savefig('graphs/ploting_multypel_stocks.png')

def main():
    dates = pd.date_range('2020-01-01', '2020-12-31')
    symbols = ['AAPL', 'FB', 'GLD', 'IBM', 'KO']
    df = get_data(symbols, dates)
    plot_data(df)

if __name__=="__main__":
    main()