'''
Nhoods with 0 users
We know the nhood users live in too
aggregate on the nhoods in `users` table

Gaaah panda core series Library issues
A series difference is surprisingly non-trivial with Pandas library!
'''
import pandas as pd

def empty_neighborhoods(neighborhoods: pd.DataFrame, users: pd.DataFrame):
    # nhoodCounts = users.groupby(['neighborhood_id'])['neighborhood_id'].count()
    nhoodCounts = users.value_counts(subset = ['neighborhood_id'], sort=False).reset_index()
    # print(nhoodCounts)
    # print(type(nhoodCounts))
    nonZeroHoods = nhoodCounts['neighborhood_id'].drop_duplicates()
    allNHoods = neighborhoods['id'].drop_duplicates()
    # delta = allNHoods.subtract(nonZeroHoods)
    # diff = allNHoods[allNHoods != nonZeroHoods]
    # merged = pd.merge(nonZeroHoods.reset_index(), allNHoods.reset_index(), on=0, how='outer', indicator=True)
    # print(merged)
    # delta = set(allNHoods) - set(nonZeroHoods)
    delta = allNHoods[~ allNHoods.isin(nonZeroHoods)].index.values
    finalDf = pd.DataFrame(columns=['name'])
    for idx in delta:
        finalDf = finalDf.append({'name':neighborhoods.iloc[idx]['name']}, ignore_index=True)
    return finalDf            
