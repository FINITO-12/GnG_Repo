import mysql.connector as connector
class Database():
    def __init__(self, username: str, password: str, host: str, database: str):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    def openConnection(self):
        try:
            base = connector.connect(username=self.username,
                                     password=self.password,
                                     host=self.host,
                                     database=self.database)
        ## NOT READY