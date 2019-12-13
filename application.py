import mysql.connector
from mysql.connector import Error
from Database.Params.db_params import params


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(**params)
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()








