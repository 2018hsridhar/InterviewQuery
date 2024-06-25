'''
Fill in missing data due to telemetry issue.
Interpolate missing cell entries

Time-series dataframe : ordered by time
No 2 day missing : always one -> row below and abovei

Fill null vals in preprocessing
URL = https://www.interviewquery.com/questions/interpolating-missing-temperatures

'''
import pandas as pd

def interpolating_missing_temperatures(temperature_data: pd.DataFrame):
    # temperature_data.sort_values(by=['date'],inplace=True)
    # first and last default have vals -> no dir concern
    temperature_data['temperature'].interpolate(limit_direction='forward',inplace=True)
    return temperature_data
