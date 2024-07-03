'''
Why do we keep analyzing online shopping companies?
URL := https://www.interviewquery.com/questions/first-touch-attribution

Attribution ( to which session visit )?
Get first touch attribution ( for the users which converted ) := channel associated ( at first discovery )

First website discovery ( aqttribution ) != conversion event ( downstream later )
Need attributions before conversions occured

18 mins to solutioning :-)

'''
import pandas as pd

# [1] : Identify converted users : gaaah inefficiecnt join
def getConvertedUsers(attribution: pd.DataFrame, user_sessions: pd.DataFrame):
    convertedUsers = pd.merge(user_sessions,attribution,how='inner',left_on='session_id',right_on='session_id')
    convertedUsers = convertedUsers[convertedUsers['conversion'] == True]
    convertedUsers = convertedUsers['user_id']
    # in-place ops : returns NONE ( save on return storage )
    # method can return two types based on bool parameter :-) ( series or NONE )
    convertedUsers.drop_duplicates(keep='last',inplace=True)
    convertedUserSessions = user_sessions[user_sessions['user_id'].isin(convertedUsers)]
    return convertedUserSessions

def generateFirstTouchAttributionReport(convertedUserSessions: pd.DataFrame, attribution: pd.DataFrame):
    # [2] Join user sessions data and obtain first touch attribution
    firstTouchAttrs = pd.merge(convertedUserSessions,attribution,how='inner',left_on='session_id',right_on='session_id')
    firstTouchAttrs.sort_values(by=['user_id','created_at'],ascending=[True,True],inplace=True)
    firstTouchAttrs = firstTouchAttrs.groupby(['user_id']).head(1)
    analyticsCols = ['user_id','channel']
    ftaReport = firstTouchAttrs[analyticsCols]
    ftaReport.sort_values(by='user_id',inplace=True)
    return ftaReport
            
def first_touch_attribution(attribution: pd.DataFrame, user_sessions: pd.DataFrame):
    convertedUserSessions = getConvertedUsers(attribution,user_sessions)
    analyticsReport = generateFirstTouchAttributionReport(convertedUserSessions, attribution)
    return analyticsReport
