'''

URL = https://www.interviewquery.com/questions/paired-products
Transactions ( of products purchased by users ) ( 1B+ ) 
Find paired products -> top five ( and their names )
Ensure the pairings are unique : p2 = item first in alpha, p1 = second in alphabet

PairedProductCount -> not the actual quantity itself
Can also join ( created_at) ( with other created_at) 
Can cancel ( where product_id matches ) ( where created_at matches ) ( where quantity and user id matches ) -> don't

40 minutes -> but is the last
gaaah tried declaratively -> ended up doing procedurally instead

'''
import pandas as pd
import numpy as np

def paired_products(products: pd.DataFrame, transactions: pd.DataFrame):
    transactions.drop(columns=['quantity'],inplace=True)
    products.drop(columns=['price'],inplace=True)
    rawData = pd.merge(transactions,products,how="inner",left_on='product_id',right_on='id')
    # created_at : assume those transactions occured all @ the same time ( and that each is a pairing )
    # we may need to explode later on the list
    # we need : transactions and purchase quantity
    groupCols = ['user_id','created_at']
    productsPerUserPerTrans = rawData.groupby(by=groupCols)['name'].agg(list).reset_index()
    productsPerUserPerTrans = productsPerUserPerTrans['name']
    # stinkin generator-style syntax
    finalReport = pd.DataFrame(columns=['p1','p2'])
    for index, productList in productsPerUserPerTrans.items():
        for i in range(len(productList)):
            for j in range(i+1,len(productList),1):
                curProds = [productList[i],productList[j]]
                p1 = (min(curProds))
                p2 = (max(curProds))
                new_df = pd.DataFrame(columns=['p1','p2'], data=[[p1,p2]])
                finalReport = pd.concat([finalReport, new_df], axis=0, ignore_index=True)
    quantAgg = pd.NamedAgg(column='p1',aggfunc='count')
    finalReport = finalReport.groupby(['p1','p2']).agg(qty=quantAgg).reset_index()
    finalReport.sort_values(by=['qty'],ascending=[False],inplace=True)
    return finalReport.head(5)
