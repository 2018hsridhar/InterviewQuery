'''
URL := https://www.interviewquery.com/questions/liker-s-likers

liker_id : they are the other user, who likes me
Count number of liker's like : 

Not all likers have other likers,.
    Srinidhi can like Hari
    Pooja can like Hari
    but Pooja and Srinidhi may not have likers
    For user Hari, the likers are Srinidhi and Poojka -=> please get their count of likers

Friends -> FriendsOfFriends reasoning ( fan-out and expand the tables ).



'''
import pandas as pd
import numpy as np

def likers_likers(likes: pd.DataFrame):
    likes.drop(columns=['created_at'],inplace=True)
    friendOfFriends = pd.merge(likes,likes,how='inner',left_on='liker_id',right_on='user_id',suffixes=['_left','_right'])
    friendOfFriends.drop(columns=['user_id_left','user_id_right'],inplace=True)
    friendOfFriends.rename(columns={'liker_id_left':'user'},inplace=True)
    # don't have the group labels as the index -> bias to SQL-style grouped output
    baReport = friendOfFriends.groupby(by=['user'],as_index=False).agg(count=('liker_id_right', pd.Series.nunique))
    reportColOrder = ['count','user']
    return baReport[reportColOrder]
            
