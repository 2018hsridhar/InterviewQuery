'''
Clarified the date transactions took place/
Each `amount` is a different value

(1) Get the highest weekly revenue of 2021 -> group transactions ( by the week ) 
    can we get calendar week from DATETIME? ++col
(2) group by on weekly revenue
(2) Group by advertiser head(3) for their days later

URL = https://www.interviewquery.com/questions/best-performing-advertisers

50 minutes -> feel by isoCalendar year versus non-isoCalendar year :-) 
Please read and understand the question under ask properly!!!

The three-best performing days -> for those who hit the highest weekly revenues ( of a given week ) !!


'''
import pandas as pd
import numpy as np

# the week in itself is off ( woooh time bug ) !!! 08/01 - 08/07 ( Sunday - Saturday )
def getHighestWeeklyRevenues2021(advertisers: pd.DataFrame, revenue: pd.DataFrame):
    # STEP [1] Solve for the max weekly revenue
    highestWeeklyRevenue = revenue[['advertiser_id','transaction_date','amount']]
    highestWeeklyRevenue['transaction_date'] = pd.to_datetime(highestWeeklyRevenue['transaction_date'])
    highestWeeklyRevenue['week'] = highestWeeklyRevenue['transaction_date'].dt.strftime('%U')
    highestWeeklyRevenue['weeklyAmountByAdvertiser'] = highestWeeklyRevenue.groupby(['advertiser_id','week'])['amount'].transform(np.sum)
    maxAgg = pd.NamedAgg(column='weeklyAmountByAdvertiser',aggfunc='max')
    highestWeeklyRevenue2021 = highestWeeklyRevenue.groupby(['week']).agg(weeklyAmountByAdvertiser = maxAgg)
    maxWeeklyRevenue = highestWeeklyRevenue2021['weeklyAmountByAdvertiser'].max()
    return maxWeeklyRevenue

def best_performing_advertisers(advertisers: pd.DataFrame, revenue: pd.DataFrame):
    maxWeeklyRevenue = getHighestWeeklyRevenues2021(advertisers, revenue)
    
    weeklyRevenue = revenue[['advertiser_id','transaction_date','amount']]
    weeklyRevenue['transaction_date'] = pd.to_datetime(weeklyRevenue['transaction_date'])
    # weeklyRevenue['week'] = weeklyRevenue['transaction_date'].dt.isocalendar().week
    weeklyRevenue['week'] = weeklyRevenue['transaction_date'].dt.strftime('%U')
    weeklyRevenue['weeklyAmountByAdvertiser'] = weeklyRevenue.groupby(['advertiser_id','week'])['amount'].transform(np.sum)
    weeklyRevenue.sort_values(by=['week','amount'],inplace=True)

    # STEP [2] Solve for the advertisers with said max weekly revenues
    bestAdvertisers = weeklyRevenue[weeklyRevenue['weeklyAmountByAdvertiser'] == maxWeeklyRevenue]
    bestAdvertisers = bestAdvertisers['advertiser_id'].unique()
    advList = list(bestAdvertisers)
    bestAdvertisersTrans = weeklyRevenue.loc[weeklyRevenue['advertiser_id'].isin(advList)]
    bestAdvertisersTrans = bestAdvertisersTrans.sort_values(by=['amount'],ascending=[False])
    bestAdvertisersTrans = bestAdvertisersTrans.groupby('advertiser_id').head(3)
    bestAdvertisersTrans = pd.merge(bestAdvertisersTrans,advertisers,how='inner',left_on='advertiser_id',right_on='advertiser_id')
    bestAdvertisersTrans.drop(columns=['week','advertiser_id','weeklyAmountByAdvertiser'],inplace=True)
    bestAdvertisersTrans['transaction_date'] = pd.to_datetime(bestAdvertisersTrans['transaction_date']).dt.date
    finalReportCols = ['advertiser_name','transaction_date','amount']
    return bestAdvertisersTrans[finalReportCols]
