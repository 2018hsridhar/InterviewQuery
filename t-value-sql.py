'''
URL := https://www.interviewquery.com/questions/t-value-sql
eCommerce store products management
Check average price : single category ( versus all other categories )

Solve : t-value and DoF ( Degrees of Freedom ) 
Goal : Execute statistical testing

Commit log :
    # axis=0 ( default for series ) ( single axis ) 

    It's the two sample t-test : not the single sample t-test
    That was it : 20 minutes
    learn to compare means between two populations and check for statistical differences at the level of categorial granularity

'''
import pandas as pd
import numpy as np

def t_value_sql(products: pd.DataFrame):
    catNine = products[products['category_id'] == 9]
    notCatNine =  products[products['category_id'] != 9]
    catNinePriceAvg = catNine['price'].mean()
    catNineStdDev = catNine['price'].std(ddof=1)
    notCatNineStdDev = notCatNine['price'].std(ddof=1)
    notCatNinePriceAvg = notCatNine['price'].mean()
    sampleSizeCatNine = len(catNine.index)
    sampleSizeNotCatNine = len(notCatNine.index)
    d_o_f = sampleSizeCatNine + 1
    # t_value = (catNinePriceAvg - notCatNinePriceAvg)/ ( catNineStdDev / np.sqrt(sampleSize - 1))
    denom = (pow(catNineStdDev,2)/sampleSizeCatNine) + (pow(notCatNineStdDev,2)/sampleSizeNotCatNine)
    t_value = (catNinePriceAvg - notCatNinePriceAvg)/ np.sqrt(denom)
    data = [[t_value,d_o_f]]
    statTest = pd.DataFrame(data,columns=['t_value','d_o_f'])
    return statTest
            
