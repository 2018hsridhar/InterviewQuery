'''
URL := https://www.interviewquery.com/questions/employees-before-managers
loc/iloc -> more explicit + raise errs earlier + select single col asa  datafarme :-)
'''
import pandas as pd

def employees_before_managers(employees: pd.DataFrame, managers: pd.DataFrame):
    emt = pd.merge(employees,managers,how='inner',left_on='manager_id',right_on='id')
    joinBefore = emt[emt['join_date_x'] < emt['join_date_y']]
    joinBefore['employee_name'] = joinBefore['first_name'] + ' ' + joinBefore['last_name']
    finRes = joinBefore.loc[:, ['employee_name']]
    return finRes
