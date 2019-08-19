import pyodbc

class DB_Connect():
    """A simple class for connecting to a database and performing queries"""

    def __init__(self, passed_db_username, passed_db_password, passed_database):
        """Initialize name and age variables/attributes"""
        self.passed_db_username = passed_db_username
        self.passed_db_password = passed_db_password
        self.passed_database = passed_database
        self.conn = None

    def __connect(self):
        """Creates connections to the database when they are needed"""
        
        self.conn = pyodbc.connect(
            'DRIVER=ODBC Driver 17 for SQL Server;'
            'SERVER=sqllab.academic.walshcollege.edu;'
            'DATABASE=' + self.passed_database + ';'
            'UID=' + self.passed_db_username + ';'
            'PWD=' + self.passed_db_password + ';'
            )

    def executeQuery(self, passed_query):
        """Executes a database query for Inserts, Updates, and Deletes"""

        if not self.conn:
            self.__connect()

        cursor = self.conn.cursor()
        cursor.execute(passed_query)

    def executeSelectQuery(self, passed_query):
        """Executes a SELECT database query and returns the results as a tuple-like structure"""

        if not self.conn:
            self.__connect()

        cursor = self.conn.cursor()
        cursor.execute(passed_query)

        return cursor.fetchall()