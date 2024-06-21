import pandas as pd

'''
Users : Excited, never been bored
Select intersect(excited,not bored)
User engagement varies over time : a few states
Advertising firm driven for ad campaigns

For those excited -> they must have NEVER been bored too!


'''
def always_excited_users(ad_impressions: pd.DataFrame):
    excitedUsers = ad_impressions[ad_impressions['impression_id'] == 'Excited']['user_id']
    # notBoredUsers = ad_impressions[ad_impressions['impression_id'] != 'Bored']['user_id']
    boredUsers = ad_impressions[ad_impressions['impression_id'] == 'Bored']['user_id']
    # s1 = pd.merge(excitedUsers, notBoredUsers, how='inner', on=['user_id'])
    # distinctUserIds = s1['user_id'].unique()
    # return pd.DataFrame(distinctUserIds)
    # distinctUserIds = excitedUsers.intersect(notBoredUsers)
    # print(excitedUsers)
    # print(notBoredUsers)
    # distinctUserIds = pd.merge(excitedUsers, notBoredUsers, how='inner').drop_duplicates()
    distinctUserIdsExcitedNotBored = excitedUsers[~excitedUsers.isin(boredUsers)].drop_duplicates()
    # df[~df['team'].isin(values_list)]
    return pd.DataFrame(distinctUserIdsExcitedNotBored)




            
