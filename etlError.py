'''
ETL errors in upstream pipelines
For each employee, get current salary
No duplicate name combinations

Why are payroll schemas so common?
We need the current ( latest most up to date ) info :
    treat most recent ID as what to take too!

URL := https://www.interviewquery.com/questions/employee-salaries-etl-error
'''
import pandas as pd

def employee_salaries_etl_error(employees: pd.DataFrame):
    maxIdByName = employees.groupby(['first_name','last_name'], as_index=False).agg(mostRecentId=('id','max')).reset_index()
    salaryOnlyTable = employees.drop(['first_name','last_name','department_id'], axis=1)
    joined = pd.merge(maxIdByName,salaryOnlyTable,how="inner",left_on="mostRecentId",right_on="id")
    targetCols = ['first_name','last_name','salary']
    return joined[targetCols]
            
