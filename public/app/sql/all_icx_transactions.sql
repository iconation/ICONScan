SELECT 
    blockid,
    DATE(FROM_UNIXTIME(timestamp DIV 1000000)),
    txfrom,
    txto,
    CAST((txamount/1000000000000000000) AS UNSIGNED INTEGER),
    itxfrom,
    itxto,
    CAST((itxamount/1000000000000000000) AS UNSIGNED INTEGER)
FROM
    iconation.block
        LEFT JOIN
    (SELECT 
        transaction.block AS blockid,
            transaction.from AS txfrom,
            transaction.to AS txto,
            transaction.amount AS txamount,
            internal_transaction.from AS itxfrom,
            internal_transaction.to AS itxto,
            internal_transaction.amount AS itxamount
    FROM
        transaction
    LEFT JOIN internal_transaction ON internal_transaction.transaction = iconation.transaction.id
        AND internal_transaction.token_type = 0) AS all_transactions ON all_transactions.blockid = iconation.block.id