'''
Sort by product id and date -> then compute a cummulative summation
URL = https://www.interviewquery.com/questions/cumulative-sales-by-product
'''
import pandas as pd

def cumulative_sales_by_product(sales: pd.DataFrame):
    # Along an axis sorting
    # Excel spreadsheet emulations
    groupByList = ['product_id','date']
    sales.sort_values(by=groupByList, ascending=[True,True], inplace=True)
    # print(list(sales))
    sales['cumulative_sum'] = sales[['product_id','date','price']].groupby(['product_id']).cumsum(skipna=True)
    targetList = ['product_id','date','cumulative_sum']
    finalDF = sales[targetList]
    return finalDF
