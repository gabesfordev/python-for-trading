import pandas as pd

def get_mean_volume(symbol):
    """
    Returns mean volume
    """
    df = pd.read_csv(("data/{}.csv").format(symbol))
    return df['Volume'].mean()

def main():
    print("Mean volume")
    for symbol in ['AAPL', 'IBM']:
        print(symbol + ': ', get_mean_volume(symbol))


if __name__ == "__main__":
    main()