from mysql.connector import connect
from mysql.connector import Error

class DatabaseConnect:
    _instance = None
    _connection = None
    _cursor = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_connect(self):
        if self._connection is None or not self._connection.is_connected():
            try:
                self._connection = connect(
                    host="localhost",
                    user="root",
                    password="admin28",
                    database="hotel_motel"
                )
                self._cursor = self._connection.cursor()
            except Error as e:
                print(f"Error connecting to MySQL database")
                return None, None
            return self._connection, self._cursor
    
    def close_connection(self):
        if self._cursor:
            self._cursor.close()
        if self._connection and self._connection.is_connected():
            self._connection.close()

db = DatabaseConnect()

def connect_to_mysql():
    return db.get_connect()

def close_db_connection():
    db.close_connection()
                




'''def connect_to_mysql():
    
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="admin28",
            database="hotel_motel"
        )
        cursor = connection.cursor()
        return connection, cursor
    except Error as e:
        raise Error(f"Error connecting to MySQL database: {e}")'''