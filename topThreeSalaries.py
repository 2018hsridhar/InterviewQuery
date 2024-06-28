'''
Assumee each dept : @ least 1 emp ( no left join complexity )
Ask table assumptinos one can make

https://www.interviewquery.com/questions/top-three-salaries

[dept_id,salary,name] ( asc,desc) order
groupby(deptId).head(3) reasoning
 exec reordering later on

 Salaries could repeat -> assume not unique
'''
import pandas as pd

def top_three_salaries(departments: pd.DataFrame, employees: pd.DataFrame):
    employees['employee_name'] = employees['first_name'] + ' ' + employees['last_name']
    employees.drop(columns=['first_name','last_name'],inplace=True)
    employees.sort_values(by=['department_id','salary'],axis=0,ascending=[True,False],inplace=True)
    report = employees.groupby('department_id').head(3)
    report = pd.merge(report,departments,left_on='department_id',right_on='id',how='inner')
    report.drop(columns=['id_x','department_id','id_y'],inplace=True)
    report.rename(columns={'name':'department_name'},inplace=True)
    reportOrder = ['employee_name','department_name','salary']
    report = report[reportOrder]
    return report
