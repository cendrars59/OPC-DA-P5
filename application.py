import mysql.connector
from mysql.connector import errorcode
from Database.Params.db_params import params


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(**params)
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.close()


if __name__ == '__main__':
    connect()








