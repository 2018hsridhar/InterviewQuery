'''
Number played  :
    inRange(5,10)
    [10,+\inf]
    We need number of players ( they may NOT be unique too ) -> careful!

Multiple sources of data ( web or non-web )
URL := https://www.interviewquery.com/questions/player-analysis
'''
import pandas as pd

def player_behaviors(players: pd.DataFrame):
    # games_played_series = players['games_played']
    # games_played_geq_10 = games_played_series.loc[lambda x : x >= 10]
    games_played_geq_10 = players[players['games_played'] >= 10]
    # games_played_btwn_5_10 = players[players['games_played'] > 5 & players['games_played'] < 10]
    games_played_btwn_5_10 = players.loc[(players['games_played'] > 5) & (players['games_played'] < 10)] #, ['id','name','games_played','registered_at']]
    # print(games_played_btwn_5_10)
    # dataFrame.loc[(btwn510_num_usersdataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
                    # ['Name','JOB']])
    geq10_num_users = games_played_geq_10['name'].drop_duplicates().size
    btwn510_num_users = games_played_btwn_5_10['name'].drop_duplicates().size
    data1 = [btwn510_num_users]
    data2 = [geq10_num_users]
    df = pd.DataFrame(list(zip(data1,data2)), columns=['players_more_than_5_to_10_games', 'players_10_plus_games'])
    return df
