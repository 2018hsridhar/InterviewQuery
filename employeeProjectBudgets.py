'''
Employee Project Budgets
URL := https://www.interviewquery.com/questions/employee-project-budgets

Steps 
(A) JOIN(employee_projects,projects)
(B) Group by ( project_id) aggr ( count(uniq(empId)), sum(budget))
(C) Sort and get head(5) here

Project's with no employees -< it's a left join : natural exclusion :-) 

20 minutes given ( time to research too ) 
Learned about named aggregates as well
'''
import pandas as pd

def employee_project_budgets(employee_projects: pd.DataFrame, projects: pd.DataFrame):
    ep = pd.merge(employee_projects,projects,how='left',left_on='project_id',right_on='id')
    agg_one = pd.NamedAgg(column="budget", aggfunc="max")
    agg_two = pd.NamedAgg(column="employee_id", aggfunc=lambda x: x.nunique())
    epPrime = ep.groupby(['project_id']).agg(totalBudget=agg_one, totalEmp=agg_two).reset_index()
    epPrime['budget_per_employee'] = (epPrime['totalBudget'] / epPrime['totalEmp'])
    epInf = pd.merge(epPrime,projects,how='inner',left_on='project_id',right_on='id')
    targetCols = ['budget_per_employee','title']
    sortKey = 'budget_per_employee'
    finalInf = epInf[targetCols]
    finalInf.sort_values(by=sortKey, inplace=True, ascending=False)
    budgetAnalytics = finalInf.head(5)
    return budgetAnalytics
