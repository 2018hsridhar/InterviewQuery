'''
Medical researcher AI work.
Split dataframe into [train,test] sets
preserve ratio

No scikit-learn usage

URL := https://www.interviewquery.com/questions/stratified-split
https://towardsdatascience.com/stratified-sampling-you-may-have-been-splitting-your-dataset-all-wrong-8cfdd0d32502

Target varaible distributions
Heterogenous population sampling
'''

import pandas as pd

# The column can differ -> but please split accordingly
# cols can be each non-index attr : age, smoking, & cancer

# .7(NO)(col) -> train and .7(YES)(col) -> train, across diff cols
train_ratio = 0.7
col = "cancer"

def stratified_split(train_ratio,col,patients: pd.DataFrame):
    patientsYes = patients[patients[col] == 'yes']
    patientsNo = patients[patients[col] == 'no']
    trainYes = patientsYes.sample(frac=0.7)
    trainNo = patientsNo.sample(frac=0.7)
    trainSetTargetClassColDim = len(trainNo.index)
    return trainSetTargetClassColDim
