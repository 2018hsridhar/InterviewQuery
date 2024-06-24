'''
Distance traveled by each user : in DESC order
1. Join Users with Rides to get names
2. Group by passenger_user_id  order by distance then grab names from said series
URL = https://www.interviewquery.com/questions/distance-traveled
'''
import pandas as pd

def distance_traveled(rides: pd.DataFrame, users: pd.DataFrame):
    # each user : all users in users table!
    users.rename(columns = {'id': 'passenger_user_id'}, inplace = True)
    # preserves left keys order ( in rides table )
    # intersect keys : ensure keys in both tables
    allCols = pd.merge(users,rides,how="left",on=['passenger_user_id'])
    # print(allCols)
    # reduce calls to .groupby using .agg
    # dictionary style aggregation desireable -> preserves column names
    # behavior : as_index = False versus .reset_index()
    distance_traveled = allCols.groupby(['name']).agg({"distance": "sum"}).sort_values(by = ['distance'], ascending=False).rename(columns={'distance':"distance_traveled"}).reset_index()
    # print(list(distance_traveled))
    dfRes = distance_traveled[['distance_traveled','name']]
    dfRes['distance_traveled'] = dfRes['distance_traveled'].astype(int)
    dfRes.set_index('distance_traveled')
    return dfRes






            
