import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("data/AAPL.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.savefig('graphs/aapl.png')

if __name__=="__main__":
    main()