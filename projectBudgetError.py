'''
URL := https://www.interviewquery.com/questions/project-budget-error
Comparison ratio : budget / employeeCount ( order ASC all projects ) -> aggregations later

20 minutes
somethig is off in an aggregation here. I can't tell

'''
import pandas as pd

def project_budget_error(employee_projects: pd.DataFrame, projects: pd.DataFrame):
    # print(employee_projects)
    # uniqEP = employee_projects[employee_projects.duplicated(subset=['project_id','employee_id'], keep=False)]
    # uniqEP = employee_projects.drop_duplicates(inplace = False)
    uniqEP = employee_projects.drop_duplicates( 
        subset = ['project_id', 'employee_id'], 
        keep = 'last').reset_index(drop = True) 
    mergedEP = pd.merge(projects,uniqEP,how='inner',left_on='id',right_on='project_id')
    # print(mergedEP)
    # preserve cols in groupby clause too?
    # It's a max =-> not a sum -> of the projects
    groupEPPrev = mergedEP.groupby(['project_id']).agg(
        totalBudget =('budget','max'),
        employeeCount=('employee_id','count'),
    ).reset_index()
    groupEP = pd.merge(groupEPPrev,projects,left_on="project_id",right_on='id',how='inner')
    targetCol = 'budget_per_employee' 
    groupEP[targetCol] = groupEP['totalBudget']/groupEP['employeeCount']
    groupEP.sort_values(by=[targetCol],inplace=True,ascending=False)
    groupEPDR = groupEP[[targetCol,'title']]
    topFiveProjects = groupEPDR.head(5)
    return topFiveProjects
    
