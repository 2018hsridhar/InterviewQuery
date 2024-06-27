'''
Regular feed analysis : analyze ads ( by users ) on a social media feed
Feed section versus moments section

Group aggregates by the ad ( not the user id ) 
No immediate horizontal concatenation.

URL := https://www.interviewquery.com/questions/ad-comments
'''
import pandas as pd

def ad_comments(ads: pd.DataFrame, feed_comments: pd.DataFrame, moments_comments: pd.DataFrame):
    # sublass of named tuples
    # Prefernece to built-in pandas functionality
    userCommentAggr = pd.NamedAgg(column='comment_id',aggfunc='count')
    momentCommentAggr = pd.NamedAgg(column='comment_id',aggfunc='count')
    # mapper / series of columns
    groupCols = ['ad_id']
    # do we need to reset the indices?
    feedComments = feed_comments.groupby(groupCols).agg(comment_count=userCommentAggr)
    momentComments = moments_comments.groupby(groupCols).agg(moment_count=momentCommentAggr)
    customerReport = pd.merge(feedComments,momentComments,how='inner',left_on='ad_id',right_on='ad_id')
    # cast objects to specified types
    customerReport['percentage_feed'] = (customerReport['comment_count'] / (customerReport['comment_count'] + customerReport['moment_count']))
    customerReport['percentage_moments'] = (customerReport['moment_count'] / (customerReport['comment_count'] + customerReport['moment_count']))
    customerReport = pd.merge(customerReport, ads, how='inner',left_on='ad_id',right_on='id')
    customerReport.drop(columns=['comment_count','id','moment_count'],inplace=True,axis=1)
    reportColsOrder = ['name','percentage_feed','percentage_moments']
    customerReport = customerReport.reindex(reportColsOrder, axis=1)
    return customerReport


            
