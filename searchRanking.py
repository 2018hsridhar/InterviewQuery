'''
Social media searches
Human ratings of search results
Position of search results crucial

Single aggr -> (all ratings < 3 ) for the query result
Relevance scoring

all the ratings ( for the query ) < 3 : ohhh ID queries rating >= 3 and drop those later?
Get unique queries ( by result id ) -> nope it's by QUERY text

URL = https://www.interviewquery.com/questions/search-ranking
'''
import pandas as pd

def search_ranking(search_results: pd.DataFrame):
    rateThreshold = 3
    ratingMoreThanThree = search_results[search_results['rating'] >= rateThreshold]
    ratingMoreThanThreeId = ratingMoreThanThree['result_id'].unique()
    ratingMoreThanThreeQuery = ratingMoreThanThree['query'].unique()
    numUniqueQueryTerms = search_results['query'].unique().size
    # series accessor : no use len() func -> use .size property
    countMoreThanThree = ratingMoreThanThreeQuery.size
    # treated as numpy.ndarray ( a pd data frame )?
    countLessThanThree = numUniqueQueryTerms - countMoreThanThree
    finalAggr = round(countLessThanThree / (countLessThanThree + countMoreThanThree),2)
    data = [[finalAggr]]
    df = pd.DataFrame(data,columns=['percentage_less_than_3'])
    return df
