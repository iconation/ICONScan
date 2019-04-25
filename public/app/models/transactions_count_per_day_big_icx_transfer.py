import json

class TransactionsCountPerDayBigIcxTransfer:
    def __init__ (self, db):
        db.sql.execute (open ("app/sql/transactions_count_per_day_big_icx_transfer.sql", "rb").read())
        self.result = db.sql.fetchall()
    
def process (db):
    return TransactionsCountPerDayBigIcxTransfer(db).result
