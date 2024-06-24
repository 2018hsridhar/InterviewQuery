import pandas as pd

'''
URL := https://www.interviewquery.com/questions/acceptance-rate
Have all requests ( f1,f2) and acceptances (f1,f2)
requester id in both tables -> can we join here?
or can we group by as well?

requester_id : have a number (requested_id) and (acceptor_id)
we need a set intersection : acceptors id and requested id
ignore created_at

cartesian join idea? no on keyword -> all columns used in the `.merge` method

'''

def acceptance_rate(friend_accepts: pd.DataFrame, friend_requests: pd.DataFrame):
    joinedFriends = friend_accepts.merge(friend_requests,how='cross').reset_index()
    reqId = joinedFriends[['acceptor_id','requester_id_x','requester_id_y','requested_id']]
    acceptedReqs = reqId[(reqId['acceptor_id'] == reqId['requested_id']) & (reqId['requester_id_x'] == reqId['requester_id_y'])]
    numAccepted = len(acceptedReqs.index)
    numRequests = len(friend_requests.index)
    total = numAccepted / numRequests
    finalData = [total]
    finalDF = pd.DataFrame(finalData, columns=['acceptance_rate'])
    return finalDF
            
