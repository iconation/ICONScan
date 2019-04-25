
class AllTransactions:
    def __init__ (self, db):
        db.sql.execute (open ("app/sql/all_icx_transactions.sql", "rb").read())
        self.result = db.sql.fetchall()

def process (db):
    return AllTransactions(db).result
