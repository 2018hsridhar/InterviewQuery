'''
Why is Python 3.1 used for pandas?
2nd highest ( by distinct )

Dataframe cols = series
Object selection -> location based indexing

'''
import pandas as pd

def second_highest_salary(departments: pd.DataFrame, employees: pd.DataFrame):
    engDeptIdList = departments.index[departments['name']=="engineering"].tolist()
    engDeptIdIdx = (int)(engDeptIdList[0])
    engDeptId = departments['id'][engDeptIdIdx]
    # first step : get only engineering department values
    engDeptRows = employees[employees['department_id'] == engDeptId]
    # second step : get the unique salaries within the department
    uniqSalaries = engDeptRows['salary'].sort_values(ascending=False).unique()
    # oh -> create a new dataframe ( woah )
    result = uniqSalaries[1]
    data = [result]
    df = pd.DataFrame(data)
    df.columns = ['salary']
    return df



    
            
