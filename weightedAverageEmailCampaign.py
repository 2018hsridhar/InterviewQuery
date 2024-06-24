'''
https://www.interviewquery.com/questions/weighted-average-email-campaign
Stinking conversion to floats for columns
'''
import pandas as pd

def weighted_average_email_campaign(email_campaigns: pd.DataFrame):
    ecf = email_campaigns.astype({"num_users":'float', "num_opens":'float', "num_clicks":"float"})  
    ecf['weighted_avg'] = (((0.3 * ecf['num_opens'])/(ecf['num_users'])).round(2) + ((0.7 * ecf['num_clicks'])/(ecf['num_users'])).round(2)).round(2)
    finalRes = ecf[['campaign_name','weighted_avg']]
    return finalRes
