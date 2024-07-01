'''
URL := https://www.interviewquery.com/questions/sequentially-fill-in-integers

One integer value per row : sequential manner
Number is repeated by one times it's own value -> frequency appending

Pandas even needed for data scientists?

'''
import pandas as pd

def sequentially_fill_in_integers(tbl_numbers: pd.DataFrame):
    finalReport = pd.DataFrame(columns=['seq_numbers'])
    # avoid .iterrows() : seen as anti-pattern ( iteration )
    for index, row in tbl_numbers.iterrows():
        number = row['int_numbers']
        upperBound = number + 1
        for nextVal in range(1,upperBound,1):
            concatList = [finalReport, pd.DataFrame([[number]], columns=finalReport.columns)]
            finalReport = pd.concat(concatList, ignore_index=True)
    return finalReport
