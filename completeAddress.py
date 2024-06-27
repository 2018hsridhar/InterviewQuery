'''
Give this a break -> went over board ( to long )
It was honestly a space issue : simplified massively elsewhere

URL = https://www.interviewquery.com/questions/complete-addresses
'''
import pandas as pd

def complete_address(df_addresses: pd.DataFrame, df_cities: pd.DataFrame):
    # easier than you think : just 3 commas to operate on -> we could split better here TBH
    delimeter = ', '
    df_addresses[['street', 'city','zip']] = df_addresses['address'].str.split(delimeter, expand=True)
    df_addresses.drop(['address'], axis=1,inplace=True)
    colsToSplit = ['street','city','zip']
    for col in colsToSplit:
        df_addresses[col] = df_addresses[col].str.strip()
    allPieces = pd.merge(df_addresses,df_cities,how='inner',on='city')
    # lambda operation each row : df.apply(lambda) make new column
    # lambdas more generic
    allPieces['address'] = allPieces.apply(lambda x:'%s, %s, %s, %s' % (x['street'],x['city'],x['state'],x['zip']),axis=1)
    dropCols = ['street','city','zip','state']
    allPieces.drop(columns=dropCols,inplace=True)
    return allPieces


    


