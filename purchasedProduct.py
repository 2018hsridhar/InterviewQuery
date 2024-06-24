'''
URL := https://www.interviewquery.com/questions/purchased-product
First time a user bought a product from own category
Which ones repeat purchases ( within category )

It is a first time purchase ( of a category ) ? Or was it purchased before ( in the category )
Category:Product 1:n mapping

id as purchase order ( please use as future sort )
Wait we have a timing aspect -> careful!!!

groupby(category) -> get rank -> apply cond -> reorder cols -> fin
'''
import pandas as pd

def purchased_product(purchases: pd.DataFrame):
    finDF = pd.DataFrame()
    catProdsGrp = purchases[['product_category','product_name','id']].sort_values(by=['product_category','id'])
    catProdsGrp['rank'] = catProdsGrp.groupby('product_category')['id'].rank(ascending=True).astype(int)
    # Custom function apply() method new col
    catProdsGrp['category_previously_purchased'] = catProdsGrp['rank'].apply(catGroup)
    targetCols = ['product_name','category_previously_purchased']
    targetIndex = 'product_name'
    orderedTrans = catProdsGrp.sort_values(by=['id'])[targetCols]
    return orderedTrans

# Need boolean value
def catGroup(rankVal):
    if rankVal == 1.0:
        return 0
    else:
        return 1
