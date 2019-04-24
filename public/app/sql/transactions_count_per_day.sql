SELECT 
    DATE(FROM_UNIXTIME(block.timestamp DIV 1000000)),
    COUNT(DISTINCT all_transactions.txid) 
FROM
    iconation.block
INNER JOIN
    (
		SELECT
			transaction.id as txid,
			transaction.block as blockid
		FROM iconation.transaction
		LEFT JOIN
			internal_transaction
		ON
			internal_transaction.transaction = iconation.transaction.id
    ) as all_transactions
    ON all_transactions.blockid = iconation.block.id
GROUP BY DATE(FROM_UNIXTIME(block.timestamp DIV 1000000))