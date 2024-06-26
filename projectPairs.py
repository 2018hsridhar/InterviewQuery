'''
Can be any other project -> seems like an inner join here TBH
Or a cross join too
Just don't join yourself at lesat

Preference for self join : the better, lesser known join

URL := https://www.interviewquery.com/questions/project-pairs
'''
import pandas as pd

def project_pairs(projects: pd.DataFrame):
    projects.drop(['budget'], axis=1, inplace=True)
    projects.rename(columns={'title':'project_title'},inplace=True)
    pairs = pd.merge(projects,projects, left_on="end_date", right_on="start_date", how="inner", suffixes=['_start','_end'])
    pairs = pairs[pairs['id_start'] != pairs['id_end']]
    esPairs = pairs[pairs['end_date_start'] == pairs['start_date_end']]
    targetCols = ['start_date_end','project_title_start', 'project_title_end']
    finalCols = esPairs[targetCols]
    # gaaah @ this poor naming though!
    finalCols.rename(columns={'start_date_end':'date','project_title_end':'project_title_start','project_title_start':'project_title_end'},inplace=True)
    # print(finalCols)
    finalCols.set_index('date')
    finalCols['date'] = pd.to_datetime(finalCols['date'])
    # print(list(df_pairs))
    return finalCols



