'''
Subscription Overlap
URL := https://www.interviewquery.com/questions/subscription-overlap

Filter out subscriptions that do NOT have a recorded `end_date` ( `end_date` field is NA ) 

(A) Cross join execute hasOverlap(...) check
(B) Cartesian product of both frames
'''
import pandas as pd

def subscription_overlap(subscriptions: pd.DataFrame):
    # named series objects
    subPairs = pd.merge(subscriptions,subscriptions, how='cross', suffixes=['_left','_right'])
    subPairs = subPairs[subPairs['user_id_left'] != subPairs['user_id_right']]
    overlapIndexes = subPairs.index[
        ((subPairs['start_date_left'] <= subPairs['start_date_right']) & (subPairs['start_date_right'] <= subPairs['end_date_left']))
        |
        ((subPairs['start_date_left'] <= subPairs['end_date_right']) & (subPairs['end_date_right'] <= subPairs['end_date_left']))
        |
        ((subPairs['start_date_left'] >= subPairs['start_date_right']) & (subPairs['end_date_left'] <= subPairs['end_date_right']))
        |
        ((subPairs['start_date_right'] >= subPairs['start_date_left']) & (subPairs['end_date_right'] <= subPairs['end_date_left']))
    ]
    # print(overlapIndexes)
    subPairs.drop_duplicates(subset=['user_id_left','user_id_right'],keep='first',inplace=True)
    subPairs['overlap'] = 0
    subPairs.loc[overlapIndexes, 'overlap'] = 1
    finalReport = subPairs.groupby(['user_id_left'])['overlap'].max().reset_index()
    finalReport.rename(columns={'user_id_left':'user_id'},inplace=True)
    targetCols = ['overlap','user_id']
    return finalReport[targetCols]
            
