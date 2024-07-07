-- we need to get two counts
-- no need for a group by here
-- https://www.interviewquery.com/questions/order-addresses
-- 
WITH shippedToPrimary AS (
    SELECT COUNT(*) AS shippedToPrimary FROM Users AS U
    INNER JOIN transactions AS T
    ON (U.id = T.user_id)
    WHERE (address = shipping_address)
), shippedToOther AS (
    SELECT COUNT(*) AS shippedToOther FROM Users AS U
    INNER JOIN transactions AS T
    ON (U.id = T.user_id)
    WHERE (address != shipping_address)
) SELECT (SP.shippedToPrimary)/(SP.shippedToPrimary + SO.shippedToOther) AS home_address_percent
    FROM shippedToPrimary AS SP, shippedToOther AS SO
 
-- SELECT SUM(CASE WHEN (address = shipping_address) THEN 1 ELSE 0 END) AS shippedToPrimary,
-- SELECT SUM(CASE WHEN (address!= shipping_address) THEN 1 ELSE 0 END) AS shippedToOther,
-- (shippedToPrimary)/(shippedToPrimary + shippedToOther) as `home_address_percent`
-- FROM CTE1
