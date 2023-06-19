import mysql.connector


class Database:
    def __init__(self, username: str, password: str, host: str, database: str):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

    def getHost(self):
        return self.host

    def getUsername(self):
        return self.username

    def getDatabase(self):
        return self.database

    def connect(self):
        conn = mysql.connector.connect(host=self.host,
                                       username=self.username,
                                       password=self.password,
                                       database=self.database)
        return conn

    def disconnect(self, conn: mysql.connector.MySQLConnection):
        if conn.is_connected():
            conn.close()

    def createCursor(self, conn: mysql.connector.MySQLConnection):
        cursor = conn.cursor(buffered=True)
        return cursor

    def closeCursor(self, conn: mysql.connector.MySQLConnection):
        if conn.is_connected():
            conn.cursor().close()

    def insert(self, sql):
        pass