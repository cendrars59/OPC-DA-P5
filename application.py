# -*- coding: Utf-8 -*
from Database.dbRessources import connect
from Database.dbRessources import create_database
from Utils.datafeed import feed_application
from mysql.connector import errorcode





def main():
    connection = connect()
    
    if connection == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check database credential")
    elif connection == errorcode.ER_BAD_DB_ERROR:
        print('Database is not created')
        print('Database will be created and data inserted')
        print('it will take a while. Have a break')
        create_database()
        connection = connect()
        # data feed 
        print('settings done')

    print("yolo")
    feed_application(connection)

if __name__ == '__main__':
    main()








