import pandas as pd

def get_max_close(symbol):
    """Returns maximum closing price for stock indicated by symbol.
    """
    df = pd.read_csv(("data/{}.csv").format(symbol))
    return df['Close'].max()

def main():
    print("Max close:")
    for symbol in ['AAPL', 'IBM']:
        print(symbol + ': ', get_max_close(symbol))


if __name__ == "__main__":
    main()