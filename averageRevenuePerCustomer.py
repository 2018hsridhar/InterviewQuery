'''
B2B SaaS company with some tenure.
Revenue lines : service, software
    hourly rate versus subscription

Clientale average revenue
URL = https://www.interviewquery.com/questions/average-revenue-per-customer
'''
import pandas as pd

def average_revenue_per_customer(payments: pd.DataFrame):
    targetName = 'average_lifetime_revenue'
    payments[targetName] = payments.apply(createCol, axis=1)
    targetSeries = payments[targetName]
    # averageVal = round(targetSeries.mean(),2)
    numUniqClients = payments['user_id'].drop_duplicates().size
    averageValAcrossClients = round(targetSeries.sum() / numUniqClients ,2)
    data = [averageValAcrossClients]
    df = pd.DataFrame(data, columns=[targetName])
    return df

# Function approach -> append a col
def createCol(row):
    alr = 0
    if row['product_type'] == 'service':
        alr = row['amount_per_unit'] * (float)(row['quantity'])
    elif row['product_type'] == 'software':
        alr = row['amount_per_unit']
    return alr
    
