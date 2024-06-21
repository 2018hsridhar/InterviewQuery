'''
Good Grades and Favorite Colors
Filters on dataframes non-trivial
Learn boolean indexing
<class 'pandas.core.frame.DataFrame'>
    ^ Plesae check the type!
Careful on series operators : and vs &, or vs |
'''
import pandas as pd

def grades_colors(students_df: pd.DataFrame):
    # greenOrRedRows = students_df[students_df['favorite_color'] == 'green' or students_df['favorite_color'] == 'red']
    # df.loc[((df['col1'] == 'A') & (df['col2'] == 'G'))]
    # greenOrRedRows = students_df.loc[((students_df['favorite_color'] == 'green') or (students_df['favorite_color'] == 'red'))]
    # greenRows = (students_df['favorite_color'] == 'green')
    # redRows = (students_df['favorite_color'] == 'red')
    # print(greenOrRedRows)
    # print(greenRows)
    # print(redRows)
    # greenRows = students_df[(students_df['favorite_color'] == 'green')]
    # greenOrRedRows = students_df[(students_df['favorite_color'] == 'green') | (students_df['favorite_color'] == 'red')]
    # print(greenOrRedRows)    
    # print(type(greenOrRedRows))
    # return None
    # gradeAbove90 = greenOrRedRows.loc[(greenOrRedRows['grade'] > 90)]
    # gradeAbove90 = greenOrRedRows[(greenOrRedRows['grade'] > 90)]
    gradeAbove90 = students_df[((students_df['favorite_color'] == 'green') | (students_df['favorite_color'] == 'red')) & (students_df['grade'] > 90)]
    return gradeAbove90
    # return pd.DataFrame(gradeAbove90)


