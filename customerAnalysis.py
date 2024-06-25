'''
Summary level info on customer purchases
Most recent purchase = the latest purchase
Order count = total number of purchases

URL := https://www.interviewquery.com/questions/customer-analysis
Commit log :

'''
import pandas as pd

def customer_analysis(df):
    finalCols = ['customer_id','gender','most_recent_sale','order_count']
    # customerAggrs = df.groupby(['customer_id']).agg(order_count=('date of sale','count'),most_recent_sale=('date of sale','max')).reset_index()
    df['order_count'] = df.groupby(['customer_id'])['date of sale'].transform('count')
    df['most_recent_sale'] = df.groupby(['customer_id'])['date of sale'].transform('max')
    finalDF = df[finalCols].drop_duplicates(subset=['customer_id'])
    return finalDF
