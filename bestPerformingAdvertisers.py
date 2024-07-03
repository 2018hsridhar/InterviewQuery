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

Nasty-ass bug :
    # weeklyRevenue['week'] = weeklyRevenue['transaction_date'].dt.isocalendar().week
    highestWeeklyRevenue['week'] = highestWeeklyRevenue['transaction_date'].dt.strftime('%U')

'''
import pandas as pd
import numpy as np

# the week in itself is off ( woooh time bug ) !!! 08/01 - 08/07 ( Sunday - Saturday )
def getHighestWeeklyRevenues2021(advertisers: pd.DataFrame, revenue: pd.DataFrame):
    # STEP [1] Solve for the max weekly revenue
    filterCols = ['advertiser_id','transaction_date','amount']
    highestWeeklyRevenue = revenue[filterCols]
    highestWeeklyRevenue['transaction_date'] = pd.to_datetime(highestWeeklyRevenue['transaction_date'])
    highestWeeklyRevenue['week'] = highestWeeklyRevenue['transaction_date'].dt.strftime('%U')
    highestWeeklyRevenue['weeklyAmountByAdvertiser'] = highestWeeklyRevenue.groupby(['advertiser_id','week'])['amount'].transform(np.sum)
    return highestWeeklyRevenue

def getThreeBestPerfDaysPerAdvertiser(advertisers: pd.DataFrame, weeklyRevenue: pd.DataFrame):
    maxWeeklyRevenue = weeklyRevenue['weeklyAmountByAdvertiser'].max()
    bestAdvertisers = weeklyRevenue[weeklyRevenue['weeklyAmountByAdvertiser'] == maxWeeklyRevenue]
    advList = bestAdvertisers['advertiser_id'].unique()
    bestAdvertisersTrans = weeklyRevenue.loc[weeklyRevenue['advertiser_id'].isin(advList)]
    bestAdvertisersTrans = bestAdvertisersTrans.sort_values(by=['amount'],ascending=[False])
    bestAdvertisersTrans = bestAdvertisersTrans.groupby('advertiser_id').head(3)
    bestAdvertisersTrans = pd.merge(bestAdvertisersTrans,advertisers,how='inner',on='advertiser_id')
    bestAdvertisersTrans.drop(columns=['week','advertiser_id','weeklyAmountByAdvertiser'],inplace=True)
    bestAdvertisersTrans['transaction_date'] = pd.to_datetime(bestAdvertisersTrans['transaction_date']).dt.date
    finalReportCols = ['advertiser_name','transaction_date','amount']
    finalReport = bestAdvertisersTrans[finalReportCols]
    return finalReport

def best_performing_advertisers(advertisers: pd.DataFrame, revenue: pd.DataFrame):
    weeklyRevenue = getHighestWeeklyRevenues2021(advertisers, revenue)
    finalReport = getThreeBestPerfDaysPerAdvertiser(advertisers, weeklyRevenue)
    return finalReport
