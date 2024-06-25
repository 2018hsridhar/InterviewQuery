'''
Number users posted a job :
(A) Once only
(B) Multiple times
each user has @ least one job posting :-)
verify : sum meets # ( programatically too ) ?

User:job 1:n mapping 
    Group by : (UserId,JobId), count(other_attr)
    Nested list based here

'''
import pandas as pd

def repeat_job_postings(job_postings: pd.DataFrame):
    jobAggr = job_postings.groupby(['user_id','job_id']).agg(post_number=('job_id','count')).reset_index()
    numDistinctUsers = len(jobAggr['user_id'].drop_duplicates())
    moreThanOnePost = jobAggr[jobAggr['post_number'] >= 2]
    multiple_posts = len(moreThanOnePost['user_id'].drop_duplicates())
    single_post = numDistinctUsers - multiple_posts
    data = [[single_post,multiple_posts]]
    analytics = pd.DataFrame(data, columns=['single_post','multiple_posts'])
    return analytics



            
