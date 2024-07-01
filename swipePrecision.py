'''
URL := https://www.interviewquery.com/questions/swipe-precision

Users have variants of AB tests?
Analyze mean number of swipes

Variant -> get
a: number of users
b: mean right swipes
c. the 3 thresholds ( 10,50,100 )

Feed change experiments
Exclude users : < 10 total swipes ( not just right swipes )
Get count of user swipes ( in experiments first ) 

Break down problem

35 minutes ( but solved ) :-)

'''
import pandas as pd

def swipe_precision(swipes: pd.DataFrame, variants: pd.DataFrame):
    nrsAgg = pd.NamedAgg(column="is_right_swipe", aggfunc="count")
    nsAgg = pd.NamedAgg(column="is_right_swipe", aggfunc=(lambda x : (x == True).sum()))
    userSwipeCounts = swipes.groupby(['user_id']).agg(num_swipes=nrsAgg,num_right_swipes=nsAgg).reset_index()
    userSwipeCounts = userSwipeCounts[userSwipeCounts['num_swipes'] >= 10]
    allDataPreThresholds = pd.merge(userSwipeCounts,variants,how='inner',left_on='user_id',right_on='user_id')
    swipeThresholds = pd.Series([10,50,100],name='swipe_threshold')
    allDataWithThresholds = pd.merge(allDataPreThresholds,swipeThresholds,how='cross')
    allDataWithThresholds = allDataWithThresholds[allDataWithThresholds['num_swipes'] == allDataWithThresholds['swipe_threshold']]
    finalData = allDataWithThresholds
    filterCols  = ['variant','num_right_swipes','swipe_threshold','user_id']
    finalData = finalData[filterCols]
    mrsAgg = pd.NamedAgg(column='num_right_swipes',aggfunc='mean')
    nuAgg = pd.NamedAgg(column='user_id',aggfunc='count')
    finalReport = finalData.groupby(['variant','swipe_threshold']).agg(mean_right_swipes=mrsAgg,num_users=nuAgg).reset_index()
    finalOrder  = ['variant','mean_right_swipes','swipe_threshold','num_users']
    return finalReport[finalOrder]





    return swipes
            
