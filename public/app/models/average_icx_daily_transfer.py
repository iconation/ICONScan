import json

class ICXAverageTransferAmountPerDayStat:
    def __init__ (self, db):
        db.sql.execute (open ("app/sql/average_icx_daily_transfer.sql", "rb").read())
        self.result = db.sql.fetchall()
    
def process (db):
    return ICXAverageTransferAmountPerDayStat (db).result
