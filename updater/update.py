import mysql.connector # pip3 install mysql-connector-python
import datetime, calendar, json

def date_json_serializer (obj):
    return obj.isoformat()

class TransactionsCountPerDayStat:
    def __init__ (self, updater):
        updater.cursor.execute (open("sql/transactions_count_per_day.sql", "rb").read())
        self.result = json.dumps (updater.cursor.fetchall(), default=date_json_serializer)
    
    def export (self, destination):
        open (destination, "wb+").write (self.result)

class IconScanUpdater:

    def __init__ (self, credentials_filename):
        self.credentials = json.loads (open (credentials_filename, "r").read())

    def connect_to_mysql (self):
        self.db = mysql.connector.connect (
            host = "localhost", 
            user = self.credentials["user"], 
            passwd = self.credentials["password"], 
            database = self.credentials["database"], 
            auth_plugin = "mysql_native_password"
        )
        self.cursor = self.db.cursor()

if __name__ == "__main__":
    updater = IconScanUpdater ("credentials.json")
    updater.connect_to_mysql()
    stats = TransactionsCountPerDayStat (updater)