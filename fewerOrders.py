'''
URL := https://www.interviewquery.com/questions/fewer-orders

Two seperate aggregations :
(A) Get count of orders per use
(B) In transactions -> users can order multiple products -> group by product ID
(C) Do as 2 seperate aggrs -> them combine them later!
    users : different products purchased -> go GROUP it! <$500 ( of product -> across all products )

Get users table last here :-)
'''
import pandas as pd

def fewer_orders(products: pd.DataFrame, transactions: pd.DataFrame, users: pd.DataFrame):
    userWithOrderCounts = transactions.groupby(['user_id']).agg(OrderCount=('product_id','count')).reset_index()
    usersLessThanThree = userWithOrderCounts[userWithOrderCounts['OrderCount'] < 3]
    userProducts = pd.merge(transactions,products,how='inner',left_on='product_id',right_on='id')
    userProducts['cost'] = userProducts['quantity'] * userProducts['price']
    userCostGroup = userProducts.groupby(['user_id']).agg(UserCost=('cost','sum')).reset_index()
    usersLessThan500 = userCostGroup[userCostGroup['UserCost'] < 500]
    metCriteriaUsers = usersLessThanThree.append(usersLessThan500).drop_duplicates(subset=['user_id'])
    userNames = pd.merge(metCriteriaUsers,users,how='inner',left_on='user_id',right_on='id')
    finalDF = userNames.rename(columns={'name': 'users_less_than'})[['users_less_than']]
    return finalDF
