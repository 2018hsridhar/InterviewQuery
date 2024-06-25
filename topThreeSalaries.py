'''
URL := https://www.interviewquery.com/questions/top-three-salaries
3 highest emp salaries : by department
top 2 or top 1 -> if not all top 3 ( shouldn't the .head(n) func still work anyways ) 
first naem concat last naem thing too

Each dept has @ least 1 employee -> can do inner join 

Return back to this later :-)
'''
import pandas as pd

def top_three_salaries(departments: pd.DataFrame, employees: pd.DataFrame):
    departments.rename(columns={'name':'department_name'},inplace=True)
    # print(departments)
    targetCols = ['employee_name','department_name','salary']
    employees['employee_name'] = employees['first_name'] + ' ' + employees['last_name']
    edt = pd.merge(employees,departments,left_on='department_id',right_on='id',how='inner')
    dimReduced = edt[targetCols]
    # print(dimReduced)
    top3Table = dimReduced.sort_values(by=['department_name','employee_name','salary'],ascending=False).groupby('department_name').head(3)
    # top3Table = top3Table.sort_values(by=['department_name'],ascending=[True])
    top3Table['lowercase'] = top3Table['department_name'].str.lower()
    top3Table = top3Table.sort_values(by=['lowercase','salary'],ascending=[True,False])
    del top3Table['lowercase']
    # hard to retrieve original columnar information back again
    return top3Table
