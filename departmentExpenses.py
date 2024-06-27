'''
Department Expenses
URL := https://www.interviewquery.com/questions/department-expenses
I can not tell if the average expense if across all departments or grouped by department
This average is over all departments ( not grouped by ) -> compute ahead of time please!

'''
import pandas as pd

def department_expenses (departments: pd.DataFrame, expenses: pd.DataFrame):
    # implcit conversion to date time ( versus DATE ) gaaah WTF Pandas library
    # handle the case of an empty expenses table too
    if(len(expenses.index) == 0):
        departments['total_expense'] = 0
        departments['average_expense'] = 0
        departments.drop(labels=['id'],axis=1,inplace=True)
        departments.rename(columns={'name':'department_name'},inplace=True)
        return departments
    expenses['date'] = pd.to_datetime(expenses['date'])
    expenses = expenses[expenses['date'].dt.year == 2022]
    # col selection = series selection
    # does need a group by ( total expense ) -> average calculated on that!
    # avgExpense = expenses.loc[:, 'amount'].mean().round(2)
    # print(expenses)
    ed = pd.merge(expenses,departments,how='right',left_on='department_id',right_on='id')
    # # print(ed)
    aggr1=pd.NamedAgg(column="amount", aggfunc="sum")
    colMap = {'name':'department_name'}
    ed.rename(columns=colMap)
    grpdAggrs = ed.groupby(['department_id']).agg(total_expense=aggr1).reset_index()
    totalExpense = grpdAggrs.loc[:, 'total_expense'].sum()
    numDepartments = len(departments.index)
    avgExpense = (totalExpense / numDepartments ).round(2)
    finalReport = pd.merge(grpdAggrs,departments,how="right",left_on='department_id',right_on='id')
    dropCols = ['department_id']
    finalReport.drop(labels=dropCols,axis=1,inplace=True)
    finalReport.rename(columns={'name':'department_name'},inplace=True)
    finalReport['average_expense'] = avgExpense
    targetCols = ['department_name','total_expense','average_expense']
    finalReport.sort_values(by=['total_expense'],ascending=False,inplace=True)
    reorderedReport = finalReport[targetCols]
    reorderedReport['total_expense'] = reorderedReport['total_expense'].fillna(0)
    return reorderedReport
