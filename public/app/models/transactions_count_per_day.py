import json

class TransactionsCountPerDay:
    def __init__ (self, db):
        db.sql.execute (open ("app/sql/transactions_count_per_day.sql", "rb").read())
        self.result = db.sql.fetchall()
    
def process (db):
    return TransactionsCountPerDay(db).result
