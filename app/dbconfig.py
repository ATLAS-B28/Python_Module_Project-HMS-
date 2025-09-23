from mysql.connector import connect
from mysql.connector import Error

def connect_to_mysql():
    """
    Establishes a connection to a MySQL database using the provided credentials.

    Args:
    host (str): The hostname or IP address of the MySQL server.
    user (str): The username for authentication.
    password (str): The password for authentication.
    database (str): The name of the database to connect to.

    Returns:
    mysql.connector.connection.MySQLConnection: A connection object if the connection is successful.

    Raises:
    mysql.connector.Error: If there's an error during the connection attempt.

    Example:
    >>> conn = connect_to_mysql('localhost', 'user', 'password', 'mydatabase')
    >>> type(conn)
    <class 'mysql.connector.connection.MySQLConnection'>
    """
    try:
        connection = connect(
            host="localhost",
            user="admin",
            password="admin28",
            database="hotel_motel"
        )
        cursor = connection.cursor()
        return connection, cursor
    except Error as e:
        raise Error(f"Error connecting to MySQL database: {e}")