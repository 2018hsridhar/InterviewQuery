'''
URL := https://www.interviewquery.com/questions/top-3-users
rank() as a window function in pandas 
File-hosting websites

Sort by date -> get histogram of users on per day basis : a groupby[day,users]
Get the daily rank -> oh we just write (1,2,3) here

Twas quick ! Awesome!!

'''
import pandas as pd

def top_3_users(download_facts: pd.DataFrame):
    udc = download_facts.sort_values(by=['date'], ascending=True).groupby(['date','user_id']).agg(downloads=('downloads','sum')).reset_index()
    N = 3
    topThreeUsersTemp = udc.sort_values(by=['date','downloads'], ascending=[True,False])
    topThreeUsersTemp['daily_rank'] = topThreeUsersTemp.groupby(['date'])['downloads'].rank(ascending=False).astype(int)
    topThreeUsers = topThreeUsersTemp.groupby(['date']).head(N)
    finalOrd = topThreeUsers.loc[:,['daily_rank','user_id','date','downloads']]
    return finalOrd
            
