'''
Woah pandas teaches pythonic-based querying of application-level dataframes!
URL = https://www.interviewquery.com/questions/third-purchase

We always sorting a business transactions table
can we sassume all users made at least 3 purchases here?

'''
import pandas as pd

def third_purchase(transactions: pd.DataFrame):
    # why do a group by when we can already sort?
    transactions.sort_values(by=['user_id','created_at','id'],ascending=[True,True,True],inplace=True)
    # head and tail not easy to combine
    transactions = transactions.groupby(by=['user_id']).head(3)
    transactions = transactions.groupby(by=['user_id']).tail(1)
    targetCols = ['user_id','created_at','product_id','quantity']
    # date object conv needs ( why ). Usually input be a string
    # transactions['created_at'] = pd.to_datetime(transactions['created_at'])
    colsToDateTimeConv = ['created_at']
    transactions[colsToDateTimeConv] = transactions[colsToDateTimeConv].apply(pd.to_datetime)
    transactions = transactions[targetCols]
    return transactions
            
