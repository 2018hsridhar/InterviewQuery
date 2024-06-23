'''
URL := https://www.interviewquery.com/questions/last-transaction
Each day -> group and sort across each date
Get the last transaction and order then
Add another column -> get the time part ( not the YYMMDD prefix )

'''
import pandas as pd

def last_transaction(bank_transactions: pd.DataFrame):
    finalTrans = bank_transactions.sort_values(
        by="created_at",
        ascending=True
    )
    finalTrans['timestamp'] = pd.to_datetime(finalTrans['created_at'])
    finalTrans['date'] = finalTrans['timestamp'].dt.strftime("%Y-%m-%d")
    finalTrans['time'] = finalTrans['timestamp'].dt.strftime("%H:%M:%S")
    finalTrans['maxTime'] = finalTrans.groupby(['date'])['time'].transform("max")
    idealTrans = finalTrans[["created_at","transaction_value", "id","time","maxTime"]]
    # print(idealTrans)
    idealTransFilter = idealTrans[idealTrans['time'] == idealTrans['maxTime']]
    finalRes = idealTransFilter[['created_at','id','transaction_value']]
    finalRes['created_at'] = pd.to_datetime(finalRes['created_at'])
    return finalRes
