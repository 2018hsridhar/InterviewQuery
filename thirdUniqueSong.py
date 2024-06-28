'''
Each user and THEIR OWN unique songs ( not unique songs across the board )
Sort table ahead of time ( date of songs played )
Drop duplicates ( within the group ) ( keep first records though )

Minimize early on JOIN() ops -> can we join tables later?

URL = https://www.interviewquery.com/questions/third-unique-song
'''
import numpy as np
import pandas as pd

def third_unique_song(song_plays: pd.DataFrame, users: pd.DataFrame):
    song_plays.sort_values(by='date_played',ascending=True,inplace=True)

    # uniqAgg = pd.NamedAgg(column='song_name',aggfunc='unique')
    # g = song_plays.groupby('user_id').agg(uniqCol=uniqAgg)
    # get grouper key error issues
    # https://stackoverflow.com/questions/55653832/pandas-groupby-keep-only-rows-with-first-occurrence
    earliestPlayDate = song_plays.groupby(['user_id','song_name'])['date_played'].min().reset_index()
    earliestPlayDate.sort_values(by='date_played',ascending=True,inplace=True)
    earliestPlayDate = earliestPlayDate.groupby('user_id').head(3)
    # transform on group by and preserve original dimensions
    earliestPlayDate['countUniq'] = earliestPlayDate.groupby('user_id')['song_name'].transform('count')
    earliestPlayDate = earliestPlayDate[earliestPlayDate['countUniq'] >= 3]
    earliestPlayDate = earliestPlayDate.groupby('user_id').tail(1)
    # print(earliestPlayDate)
    report = pd.merge(users,earliestPlayDate,how='left',left_on='id',right_on='user_id')
    report.drop(columns=['countUniq','user_id','id'],inplace=True)
    report['date_played'] = pd.to_datetime(report['date_played'])
    report = report.replace({np.nan: None})
    targetOrder = ['name','date_played','song_name']
    report = report[targetOrder]
    return report
