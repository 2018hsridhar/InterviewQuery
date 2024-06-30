'''
Building naive reccommender systems ( versus complex ones ).
Queries for creating metrics for end users.
Web page recommendation systems.


(A) Users have friends
(B) Users like pages

Queries to generate metrics per use
Don't recc what a user already likes

generate for pages that the user did NOT like ( cross join idea ) ( drop ) ?
URL = https://www.interviewquery.com/questions/liked-pages

It's more of a transform here
We need to get the delta between 
(A) The pages that our friends like versus
(B) The pages that we like
and calculate those diffs

And then get the likes for the pages our friends liked!

This is a harder problem, but you're closer ( you have the delta of page likes at least )

'''
import pandas as pd

def liked_pages(friends: pd.DataFrame, page_likes: pd.DataFrame):
    
    # [1] page likes per page ( based on the user's friends ) calculate
    userFriendsPageLikes = pd.merge(friends,page_likes,how='inner',left_on='friend_id',right_on='user_id')
    friendsPageTable = userFriendsPageLikes
    count_friends = pd.NamedAgg(column="friend_id", aggfunc="count")
    pagesByLikesOfUserFriends = friendsPageTable.groupby(['page_id','user_id_x']).agg(num_friend_likes = count_friends).reset_index()
    pagesByLikesOfUserFriends.rename(columns={'user_id_x':'user_id'},inplace=True)\
    
    # [2] Get pages a user liked, which are liked by a users friends, but not by the user itself
    pagesFriendsLike = userFriendsPageLikes.groupby('user_id_x')['page_id'].apply(list).reset_index(name='friend_liked_pages')
    pagesUserLike = page_likes.groupby(['user_id'])['page_id'].apply(list).reset_index(name='user_liked_pages')
    pagesUserFriendsLike = pd.merge(pagesUserLike,pagesFriendsLike,left_on='user_id',right_on='user_id_x',how='inner')
    pagesUserFriendsLike['page_id'] = list(pagesUserFriendsLike['friend_liked_pages'].map(set) - pagesUserFriendsLike['user_liked_pages'].map(set))
    pagesUserFriendsLike = pagesUserFriendsLike.explode('page_id').reset_index(drop=True)
    pagesUserFriendsLike.dropna(how='any',inplace=True)    #to drop if any value in the row has a nan
    
    # [3] Execute final join
    finalReport = pd.merge(pagesUserFriendsLike,pagesByLikesOfUserFriends,how='inner',left_on=['user_id','page_id'],right_on=['user_id','page_id'])
    targetCols = ['num_friend_likes','page_id', 'user_id']
    finalReport = finalReport[targetCols]
    return finalReport
