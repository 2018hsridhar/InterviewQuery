'''
URL := https://www.interviewquery.com/questions/size-of-joins
'''
import pandas as pd

def size_of_joins(ads: pd.DataFrame):
    # innerJoin = leftJoin = rightJoin = crossJoin = 0
    top3Ads = ads.head(3) # already know id = popularity
    # print(type(top3Ads))
    # top3Ads.rename(columns = {'id','top3Id'}, inplace = True)
    # print(top3Ads)
    # length of index safest row calculation
    innerJoin = len(ads.merge(top3Ads, how='inner', left_on='id', right_on='id').index)
    leftJoin = len(ads.merge(top3Ads, how='left', left_on='id', right_on='id').index)
    rightJoin = len(ads.merge(top3Ads, how='right', left_on='id', right_on='id').index)
    crossJoin = len(ads.merge(top3Ads, how='cross').index)
    join_data = [["inner_join", innerJoin],["left_join",leftJoin],["right_join",rightJoin],["cross_join",crossJoin]]
    join_types = ['join_type','number_of_rows']
    queryStats = pd.DataFrame(join_data, columns=join_types)
    # # print(queryStats)
    return queryStats
    # return top3Ads
