'''
https://www.interviewquery.com/questions/over-100-dollars
Working with two dataframes
Each transaction with total value > 100 ( a join on product ids with prices )
revenue = price * total_amount

Running into key errors is surprisingly easy with pandas dataframes

'''
import pandas as pd

def transactions_over_100(df_transactions: pd.DataFrame, df_products: pd.DataFrame):
    transPricing = df_transactions.merge(df_products, how="inner", on="product_id")
    # print(transPricing)
    # create an unattached column with an index
    transPricing["amount"] = pd.to_numeric(transPricing["amount"])
    # print(transPricing)
    unattachedCol = transPricing.apply(lambda row: row.price * row.amount, axis=1)
    transPricing['total_value'] = unattachedCol
    # print(transPricing)
    # finalDf = pd.DataFrame()
    finalDf = transPricing[transPricing['total_value'] > 100]
    finalDf = finalDf.drop('price', axis=1)
    return finalDf
