'''
URL = https://www.interviewquery.com/questions/employee-salaries
Employee-Salaries

Count number emps per departments -> get top three ( seperate table here ) 


'''
import pandas as pd

def employee_salaries(departments: pd.DataFrame, employees: pd.DataFrame):
    departments.rename(columns={'name':'department_name'},inplace=True)
    ed = pd.merge(employees,departments,how="inner",left_on='department_id',right_on='id')
    deptByEmps = ed.drop(columns=['first_name','last_name','salary','id_y'])
    # hashable type here
    numberEmpsAggr = pd.NamedAgg(column='id_x',aggfunc='count')
    deptEmpsReport = deptByEmps.groupby(['department_id']).agg(number_of_employees=numberEmpsAggr).reset_index()
    # make sure series values are unique -> helps to reason in downstream codebases.
    deptTenEmps = deptEmpsReport[deptEmpsReport['number_of_employees'] >= 10]
    deptTenEmps = pd.merge(deptTenEmps,departments,left_on='department_id',right_on='id',how='inner')
    empSalaryMoreThan100 = ed.drop(columns=['first_name','last_name'])
    aggr100Ratio = pd.NamedAgg(column='salary',aggfunc=((lambda x: (x>100000).sum()/(x>=0).sum())))
    moreThan100 = empSalaryMoreThan100.groupby(['department_id']).agg(percentage_over_100k=aggr100Ratio)
    finalReport = pd.merge(moreThan100,deptTenEmps,on='department_id',how='inner')
    targetCols = ['department_name','number_of_employees','percentage_over_100k']
    return finalReport[targetCols]
