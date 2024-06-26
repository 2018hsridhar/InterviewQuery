'''
Give this a break -> went over board ( to long )

URL := https://www.interviewquery.com/questions/complete-addresses
'''
import pandas as pd

def complete_address(df_addresses: pd.DataFrame, df_cities: pd.DataFrame):
    # resultAddrs = pd.concat([df_addresses, df_cities], axis = 1)
    # print(resultAddrs)
    # easier than you think : just 3 commas to operate on -> we could split better here TBH
    # resultAddrs['zip'] = resultAddrs['address'].str[-5:]
    # resultAddrs['prefix'] = resultAddrs['address'].apply(lambda x: x[0:len(x) - 7])
    df_addresses[['street', 'city','zip']] = df_addresses['address'].str.split(',', expand=True)
    df_addresses.drop(['address'], axis=1,inplace=True)
    df_addresses.columns = df_addresses.columns.str.strip()
    df_addresses['city'] = df_addresses['city'].str.replace(" ","")
    allPieces = pd.merge(df_addresses,df_cities,how='inner',on='city')
    print(allPieces)
    # dropCols = ['zip','city','state','prefix']
    # series method string concatenation
    # resultAddrs["address"] = resultAddrs["prefix"].str.cat(resultAddrs[["state","zip"]].astype(str), sep=",")
    # resultAddrs.drop(dropCols, axis=1, inplace=True)
    # return resultAddrs


    


