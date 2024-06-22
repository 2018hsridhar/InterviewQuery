'''
Selection by labels in Pandas
List of labels
Days it rained -> ignore 0's
Note index preservation operations with filter
https://www.interviewquery.com/questions/rain-on-rainy-days
'''
import pandas as pd

def median_rainfall(df_rain):
    # this really is obtaining a median from a list of values
    # inchesRained = df_rain.loc['Inches']
    inchesRainedWith0 = df_rain.loc[:,'Inches']
    inchesRained = inchesRainedWith0[inchesRainedWith0 != 0]
    # print(type(inchesRained))
    median = inchesRained.median()
    return median
