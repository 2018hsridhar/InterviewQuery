-- Number of messages sent between two users ( by date ) 
-- Q1 : Table-Derived insights :
-- (A) Tracking the dates where messages are more frequently sent ( versus others )
-- (B) Tracking the users which more often engage in conversations versus do not
-- (C) Tracking whcih users are more "socially-connected" than other users. Can do @ DISTINCT granularity levels too
-- Q2 : I expect the distribution to look constant on most days, with some spikes for special events or one-off days
-- URL = https://www.interviewquery.com/questions/conversations-distribution
WITH STATS2 AS (
    WITH STATS1 AS (
    SELECT user1 AS `user`, COUNT(date) AS numConvo FROM messages
    GROUP BY `user`
    UNION ALL
    SELECT user2 as `user`, COUNT(date) AS numConvo FROM messages
    GROUP BY `user`
    ) SELECT SUM(numConvo) AS num_conversations FROM STATS1
        GROUP BY `user`
) SELECT num_conversations, COUNT(num_conversations) AS `frequency` FROM STATS2
    GROUP BY num_conversations
