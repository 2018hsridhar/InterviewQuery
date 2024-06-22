'''
identitical number of times log in ( duplicate number of log ins across users )
on a given date : Jan 1st, 2022 ( scope down here )
for each number of log ins, count number of users logged in
A user can log in multiple number of times to an application on a given day

#-logins in a day   #-users
7                   3
5                   4
10                  2

Coerce date time under the hood.
Aggr of userId ( group by counts )

Are dates standardized?

'''
import pandas as pd
import datetime as dt

from datetime import date

def daily_login(user_logins: pd.DataFrame):
    value_to_check = pd.to_datetime("2022-01-01")
    # really needs a good trim function here!
    user_logins["login_date"] = pd.to_datetime(user_logins["login_date"]).dt.date
    # print(type(user_logins['login_date'][0]))
    # print(type(value_to_check))
    dateMask = user_logins['login_date'] == value_to_check
    janLogins = user_logins[user_logins['login_date'] == value_to_check]
    print(janLogins)
    userLoginCounts = janLogins.groupby('user_id').agg(number_of_logins=('user_id', 'count')).reset_index()
    # print(userLoginCounts)
    loginCounts = userLoginCounts.groupby('number_of_logins').agg(number_of_users=('number_of_logins','count')).reset_index()
    # print(loginCounts)
    return loginCounts




