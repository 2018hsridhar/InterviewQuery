'''
URL = https://www.interviewquery.com/questions/cumulative-sales-since-last-restocking
Cumulative Sales Since Last Restocking

Cummulative sales : imagine that each product has only ONE last restocking event ( and NOT more than that )
Order results by product_id

Wait is this easier -> if I join {sales,restocking} and I eliniate rows where 
date <= restock_date
And then I evaluate a cummulative sum 

19 mins to solution

'''
import pandas as pd

def cumulative_sales(products: pd.DataFrame, sales: pd.DataFrame, restocking: pd.DataFrame):
    # left join or inner join here?
    # get the last date for each restocking event ( group by ) -> everything is right : but do preprocessing above
    restocking = restocking.sort_values(['restock_date']).groupby(['product_id']).tail(1)
    pst = pd.merge(sales,products,how='inner',left_on='product_id',right_on='product_id')
    finalReport = pd.merge(pst,restocking,how='inner',left_on='product_id',right_on='product_id')
    finalReport = finalReport[finalReport['date'] >= finalReport['restock_date']]
    finalReport.sort_values(by=['product_id','date'],ascending=[True,True],inplace=True)
    saveCols = ['product_name','date','sold_count']
    finalReport = finalReport[saveCols]
    finalReport['sales_since_last_restock'] = finalReport.groupby(['product_name'])['sold_count'].cumsum()
    finalReport.drop(columns=['sold_count'],inplace=True)
    return finalReport
