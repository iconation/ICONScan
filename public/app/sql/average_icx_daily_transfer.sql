SELECT 
    DATE(FROM_UNIXTIME(block.timestamp DIV 1000000)),
    CAST(AVG(transaction.amount/1000000000000000000) AS UNSIGNED INTEGER)
FROM
    iconation.block
        INNER JOIN
    iconation.transaction ON block.id = transaction.block
WHERE block.timestamp DIV 1000000 > 1546729178
GROUP BY DATE(FROM_UNIXTIME(block.timestamp DIV 1000000))