'''
Clarified the date transactions took place/
Each `amount` is a different value

(1) Get the highest weekly revenue of 2021 -> group transactions ( by the week ) 
    can we get calendar week from DATETIME? ++col
(2) group by on weekly revenue
(2) Group by advertiser head(3) for their days later

URL = https://www.interviewquery.com/questions/best-performing-advertisers

30 minutes
Please read and understand the question under ask properly!!!
'''
import pandas as pd
import numpy as np

def best_performing_advertisers(advertisers: pd.DataFrame, revenue: pd.DataFrame):
    # STEP [1] Solve for the max weekly revenue
    weeklyRevenue = revenue[['advertiser_id','transaction_date','amount']]
    # convert arg to date time ain't in place
    weeklyRevenue['transaction_date'] = pd.to_datetime(weeklyRevenue['transaction_date'])
    weeklyRevenue['week'] = weeklyRevenue['transaction_date'].dt.isocalendar().week
    # amountAgg = pd.NamedAgg(column='amount',aggfunc='sum')
    # weeklyRevenue = weeklyRevenue.groupby('week').agg(weeklyAmount = amountAgg)
    weeklyRevenue['weeklyAmount'] = weeklyRevenue.groupby(['week','advertiser_id'])['amount'].transform(np.sum)
    # print(weeklyRevenue)
    # it's not the actual max weekly revenue -> it's the max revenue ( per week )
    # w1 : (a1,...,an) the best and w2 : (a1,...,an) the best thing

    maxWeeklyRevenue = weeklyRevenue['weeklyAmount'].max()

    # STEP [2] Solve for the advertisers with said max weekly revenues
    print(weeklyRevenue)
    bestAdvertisers = weeklyRevenue[weeklyRevenue['weeklyAmount'] == maxWeeklyRevenue]
    bestAdvertisers = bestAdvertisers['advertiser_id'].unique()
    print(bestAdvertisers)
    advList = list(bestAdvertisers)
    bestAdvertisersTrans = weeklyRevenue.loc[weeklyRevenue['advertiser_id'].isin(advList)]
    # print(bestAdvertisersTrans)
    bestAdvertisersTrans = bestAdvertisersTrans.sort_values(by=['amount'],ascending=[False])
    bestAdvertisersTrans = bestAdvertisersTrans.groupby('advertiser_id').head(3)
    bestAdvertisersTrans = pd.merge(bestAdvertisersTrans,advertisers,how='inner',left_on='advertiser_id',right_on='advertiser_id')
    # print(bestAdvertisers)
    bestAdvertisersTrans.drop(columns=['week','advertiser_id','weeklyAmount'],inplace=True)
    bestAdvertisersTrans['transaction_date'] = pd.to_datetime(bestAdvertisersTrans['transaction_date']).dt.date
    # , format='[%d/%b/%Y:%H:%M:%S', errors='coerce')
    # pd.to_datetime(bestAdvertisersTrans['transaction_date'])
    reportColOrd = ['advertiser_name','transaction_date','amount']
    return bestAdvertisersTrans[reportColOrd]
