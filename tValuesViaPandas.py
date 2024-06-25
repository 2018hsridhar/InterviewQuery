'''
Solve for test statsitics
Null hypothesis : mu = mu0

URL = https://www.interviewquery.com/questions/t-value-via-pandas
'''
import math
import pandas as pd

def t_score(mu0, df: pd.DataFrame):
    sampleMean = df['var'].mean()
    sampleStdDev = df['var'].std()
    rootSize = math.sqrt(len(df.index))
    t = (sampleMean - mu0) / (sampleStdDev / rootSize )
    return [t]
