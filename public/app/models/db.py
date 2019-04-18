import mysql.connector # pip3 install mysql-connector-python
import json

class IconScanDb:

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
        self.sql = self.db.cursor()
