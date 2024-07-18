-- Decompose the problem into their subproblems : focus 
-- on just (A) mutual friends and (B) Page likes seperately
-- Then handle blocked and already users
-- Don't join to much data in the start if it feels confusing

-- Mutual friends : double join 
-- john -> friend -> FriendOfFriends
-- match : john, FriendOfFriends
-- hang on : (Alice,John) share 3 friends in common -> get the number shared each pairing
-- https://www.interviewquery.com/questions/johns-new-best-friend
-- STEP #1 : Sovle 3 points for mutual friends ( assuming that they are not already friends )
WITH FRIENDS_DATA_ALL_USERS AS (
    SELECT U.user_id, 
            U.name, 
            F.friend_id AS `friendId`
    FROM users AS U
    INNER JOIN friends AS F
    ON U.user_id = F.user_id
), FRIEND_FRIEND_MATCH_CHECK AS (
    SELECT D.user_id, 
            D.name, 
            D.friendId, 
            E.user_id AS `otherUserId`, 
            E.friendId AS `otherFriendId`
    FROM FRIENDS_DATA_ALL_USERS AS D
    CROSS JOIN FRIENDS_DATA_ALL_USERS AS E
    WHERE D.name = "John"
    AND E.name != "John"
), MUTUAL_MATCHES AS (
    SELECT C.otherUserId, COUNT(*) AS `numMutualFriendsWithJohn`, 3 * COUNT(*) AS
    `friendship_points`
    FROM FRIEND_FRIEND_MATCH_CHECK AS C
    WHERE C.friendId = C.otherFriendId
    GROUP BY C.friendId
    ORDER BY C.friendId ASC
) SELECT * FROM MUTUAL_MATCHES


-- Use a similar structure for shared pages liked :-)
