'''
Dataframe imputation
At least one cheese not missing price info

'''
import pandas as pd
import numpy as np

def cheese_median(df):
    cheesePrices = df.loc[:, ["Price"]]
    # for i in range(len(cheesePrices)):
        # print(type(cheesePrices[i]))
    cheesePrices.dropna(inplace=True)
    medianCheesePrice = ((cheesePrices.median()))[0]
    # print(type(medianCheesePrice))
    # print(medianCheesePrice)
    # print(df)
    # df = df.replace({None: np.nan})
    # print(df)
    # df['Price'].replace('None', np.nan, inplace=True)
    # df["Price"] = pd.to_numeric(df["Price"])
    df['Price'].fillna(medianCheesePrice, inplace=True)
    return df

