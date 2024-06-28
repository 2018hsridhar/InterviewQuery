'''
URL := https://www.interviewquery.com/questions/closest-sat-scores

Self join/Cross join thing ( select away students where student ids match )
Calculate the minimum scores
Select the lexicographically highest combination ( exec .sort_values() on our dataframe ) 

Named can repeat ( but id's are unique )

We need unique pairs : (1,3) and (3,1) are the same pair
    How to get unique pairings : 
    (1,2)...(1,4) then (2,3),...(2,4)


'''
import pandas as pd

def closest_sat_scores(scores: pd.DataFrame):
    scorePairs = pd.merge(scores,scores,how='cross')
    scorePairs = scorePairs[scorePairs['id_x'] != scorePairs['id_y']]
    scorePairs['score_diff'] = (scorePairs['score_x'] - scorePairs['score_y']).abs()
    colDict = {'student_x':'one_student','student_y':'other_student'}
    scorePairs.rename(columns=colDict,inplace=True)
    targetCols = ['one_student','other_student','score_diff']
    scorePairs.drop(columns=['id_x','id_y'],inplace=True,axis=1)
    scorePairs = scorePairs[targetCols]
    scorePairs.sort_values(by=['score_diff','one_student','other_student'],ascending=[True,True,True],inplace=True)
    finalReport = scorePairs.head(1)
    return finalReport




            
