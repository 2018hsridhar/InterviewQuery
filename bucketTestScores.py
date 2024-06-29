'''
URL = https://www.interviewquery.com/questions/bucket-test-scores
Data binning/bucketing

Steps
(A) Get the count by bins
(B) Get the total count ( by the score )  -> transform col
(C) Get percentage
(D) Drop it like you mean it!

Replacement of col vals later gaaah?
'''
import pandas as pd

def bucket_test_scores(df):
    bins = [0,50,75,90,100]
    labels = ['<50','<75','<90','<100']
    df['bin'] = pd.cut(df['test score'],bins,labels=labels)
    df.drop(columns=['test score'],inplace=True)
    df.rename(columns={"bin":"test score"},inplace=True)
    namedAgg = pd.NamedAgg(column="test score", aggfunc="count")
    df['oneCol'] = 1
    df.sort_values(by='test score',ascending=True,inplace=True)
    df['binSums'] = df.groupby(['grade'])['oneCol'].cumsum()
    # grades = df['grade'].unique()
    grades = df['grade'].drop_duplicates()
    testScores = pd.Series(labels, name='test score')
    gradeScores = pd.merge(grades,testScores,how='cross')
    fullReport = pd.merge(gradeScores,df,how='left',left_on=['grade','test score'],right_on=['grade','test score'])
    cols = ['binSums']
    # Neds to be an update ( to keep in place ) 
    # cols list -> donm't update all columns ( efficiency )
    fullReport.update(fullReport.groupby(['grade'])[cols].ffill().fillna(0))
    fullReport['totalPerGrade'] = fullReport.groupby('grade')['binSums'].transform('max')
    fullReport['percentage'] = round(100 * (fullReport['binSums'] / fullReport['totalPerGrade']),2).astype(int).astype(str) + '%'
    # drop duplicates keep last
    targetCols = ['grade','test score','percentage']
    fullReport = fullReport[targetCols].drop_duplicates(subset=['grade','test score'],keep='last')
    return fullReport



    
