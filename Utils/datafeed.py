# -*- coding: Utf-8 -*
import openfoodfacts
from Database.dbRessources import connect
from Utils.Params.feedParams import params


def feed(type,request,table):
    queryForCheck = ("SELECT COUNT(*) FROM {0} WHERE code=%s".format(table))
    queryForInserting = ("INSERT INTO {0} (code,name,url) VALUES(%s,%s,%s)".format(table))
    insertCount = 0
    items_list = request
    conn = connect()
    cursor = conn.cursor()

    for item in items_list: 
        cursor.execute(queryForInserting, (item['id'],item['name'],item['url']))
        insertCount += 1
        print('{0} inserted'.format(type))
        if insertCount == 1000:
            conn.commit()
            insertCount = 0
    cursor.close()
    print("{0} feed has been done!".format(type))


def feedApp():
    feed(params["store"]["type"],params["store"]["request"],params["store"]["table"])
    feed(params["category"]["type"],params["category"]["request"],params["category"]["table"])

