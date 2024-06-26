'''
Created at is a date time -> extract year and month info -> filter
Monthly reports in a single year
per month grouping of multiple aggregations : #-users, #-trans,total_vol_amount

16 minutes fast solutioning here!
URL := https://www.interviewquery.com/questions/monthly-customer-report

'''
import datetime as dt
import pandas as pd

def monthly_customer_report(products: pd.DataFrame, transactions: pd.DataFrame, users: pd.DataFrame):
    # need to always do this conversion gaaah
    transactions['created_at'] = pd.to_datetime(transactions['created_at'], infer_datetime_format=True)
    # dt accessor datetimelike values only?
    # already <int64> here
    transactions['year'] = transactions['created_at'].dt.year
    transactions['month'] = transactions['created_at'].dt.month
    # early filter step here
    transactions = transactions[transactions['year'] == 2020]
    # print(transactions.dtypes)
    # print(transactions)
    # merge() always returns a dataframe : memory intensive
    # https://stackoverflow.com/questions/61918395/while-renaming-the-column-in-a-dataframe-error-occurred
    users.rename(columns={'id':'userId'},inplace=True)
    transactions.rename(columns={'id':'transId'},inplace=True)
    ptMerge = pd.merge(transactions,products,how="inner",left_on="product_id",right_on="id")
    ptuMerge = pd.merge(ptMerge,users,how="inner",left_on="user_id",right_on="userId")
    # cast pandas object to a datatype
    ptuMerge['amount'] = (ptuMerge['quantity'] * ptuMerge['price']).astype(int)
    # need a count ( of unique users here ) !
    monthlyReport = ptuMerge.groupby('month').agg(
        num_customers = ('userId','nunique'),
        num_orders = ('transId','count'),
        order_amt = ('amount','sum')
    ).reset_index()
    return monthlyReport
            
