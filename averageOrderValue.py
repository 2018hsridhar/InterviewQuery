'''
URL := https://www.interviewquery.com/questions/average-order-value
Average order value : binned by gender
Only by users who placed an order ( not all users )

JOIN : transactions,users by user_id
JOIN : by products table
JOIN : by sex

Multiple table joins taking place heere
20 mins
'''
import pandas as pd

def average_order_value(products: pd.DataFrame, transactions: pd.DataFrame, users: pd.DataFrame):
    # When named series is treated like a dataframe
    # do we preserve or sort keys on join?
    tuJoin = pd.merge(transactions, users, how='inner', left_on='user_id', right_on='id')
    tupJoin = pd.merge(tuJoin,products,how='inner',left_on='product_id',right_on='id')
    # filter after dim reduction ( reduce memo footprint )
    genderAov = tupJoin[['sex','quantity','price']]
    genderAov['cost'] = genderAov['quantity'] * genderAov['price']
    myFinalAov = genderAov.groupby('sex').agg(
        aov=pd.NamedAgg(column='cost', aggfunc="mean")
    ).round(2).reset_index()
    colSwap = myFinalAov[['aov','sex']]
    return colSwap



            
