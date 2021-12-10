import pandas as pd
import matplotlib.pyplot as plt

def main():

    df = pd.read_csv("data/IBM.csv")
    print(df['High'])
    df['High'].plot()
    plt.savefig('graphs/ibm.png')



if __name__=="__main__":
    main()