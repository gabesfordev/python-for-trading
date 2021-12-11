import os
import pandas as pd

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


def main():
    dates = pd.date_range('2021-01-22', '2021-01-26')
    symbols = ['AAPL', 'FB', 'GLD', 'IBM', 'KO']
    df = get_data(symbols, dates)
    print(df)

if __name__=="__main__":
    main()