import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='yolo',
                                       user='root',
                                       password='root')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            query = 'select * from category'
            cursor.execute(query)
            for value in cursor:
                print(value)

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()








