'''
URL = https://www.interviewquery.com/questions/notification-deliveries
Purchase or not -> represent as a conversion ( with value or NULL ) 
Distribution of total push notifs BEFORE a user converts
    if conv is null : drop those users ( OR get all total push notifs )
    assumption : we need to drop it!

It's a lot of joins and aggregations in the hiding.
10 minutes of dumb debugging ( wrong col name buddy ) FML

40 minutes spent ( it's a HARD ) 

Commit log :
    (A) Do NOT convert all cols to date time.
    (B) If we do not have to convert a time col to DATETIME, do  NOT convert it
    (C) Proper inequality more desireable
    (D) .dropna better over complex boolean indexing : multi-col handling easier
    (E) Length of an index better for uniqueness assertion : the known is better -> unless we use a different id column
    (F) if can write `nunique` over `count`, use `nunique` for stronger guarantee

'''
import pandas as pd

def notification_deliveries(notification_deliveries: pd.DataFrame, users: pd.DataFrame):
    # preference to modify datframes in place ( save on memory footprint ) 
    users.dropna(axis=0, subset=['conversion_date'],inplace=True)
    numUniqUsers = len(users['id'])
    finalReport = pd.merge(users,notification_deliveries,how='inner',left_on='id',right_on='user_id',suffixes=['_user','_notif'])
    finalReport = finalReport[(finalReport['created_at_notif'] <= finalReport['conversion_date'])]
    finalReport = finalReport.groupby('user_id',as_index=False).agg(total_pushes=('created_at_notif','nunique'))
    numNotifiedUsers = len(finalReport.index)
    numNotNotifiedUsers = numUniqUsers - numNotifiedUsers
    finalReport = finalReport.groupby(['total_pushes'],as_index=False).agg(frequency=('user_id','nunique'))
    finalReport = finalReport[['frequency','total_pushes']]
    # get users, with conversions, who had no push notifications
    if(numNotNotifiedUsers != 0):
        finalReport.loc[len(finalReport.index)] = [numNotNotifiedUsers,0]
    return finalReport
