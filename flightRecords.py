'''
Query to generate unique pairings of two locations ( source and dest )
(A,B) and (B,A) -> one entry only (A,B) or (B,A) : not both!
Oh the original table can have duplicates -> the new table should not have duplicates

URL = https://www.interviewquery.com/questions/flight-records


'''
import pandas as pd

def flight_records(flights: pd.DataFrame):
    finalReport = pd.DataFrame(columns=[])
    finalReport['destination_one'] = flights[['source_location','destination_location']].min(axis=1)
    finalReport['destination_two'] = flights[['source_location','destination_location']].max(axis=1)
    finalReport.drop_duplicates(inplace=True)
    return finalReport
            
