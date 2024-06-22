'''
Track user actions.
Faster solutioning -> we know ay around pandas library
https://www.interviewquery.com/questions/emails-opened
'''
import pandas as pd

def emails_opened(events: pd.DataFrame):
    action_fitler = "email_opened"
    emailOpenRows = events[events['action'] == action_fitler]
    uniqueUsersOpenedEmails = emailOpenRows['user_id'].drop_duplicates()
    countUnique = uniqueUsersOpenedEmails.size
    data = dict(num_users_open_email=countUnique)
    df = pd.DataFrame(data, index=[0])
    return df
