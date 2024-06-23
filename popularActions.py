'''
Event tracking of user actions on a platform
Actions on a platform : actions scoped down
Top 5 actions during a week and rank on num times execution
Group by -> then solve for rank -> then apply filters of top 5 on the rank

Segmentation needs for data scientists
Data-centric packages everywhere

URL = https://www.interviewquery.com/questions/popular-actions
22 minutes
'''
import pandas as pd

def popular_actions(events: pd.DataFrame):
    # Convert the date to datetime64
    events['created_at'] = pd.to_datetime(events['created_at'], format='%Y-%m-%d')
    # Filter data between two dates
    filtered_df = events.loc[(events['created_at'] >= '2020-11-22')
                        & (events['created_at'] <= '2020-11-28')]
    # aggr is done on every other column ( not in group by ) 
    actionCounts = filtered_df.groupby('action').count()[['user_id']].reset_index()
    sortedActionCounts = actionCounts.sort_values(by=['user_id'], ascending=False)
    # print(sortedActionCounts)
    sortedActionCounts['ranks'] = sortedActionCounts['user_id'].rank(method='min',ascending=False).astype('int')
    # print(sortedActionCounts)
    topFiveActions = sortedActionCounts[sortedActionCounts['ranks'] <= 5].reset_index(drop=True)
    # print(topFiveActions)
    finalActions = topFiveActions[['action','ranks']]
    # print(sortedActionCounts)
    return finalActions
        

