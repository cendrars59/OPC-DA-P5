# -*- coding: Utf-8 -*
import openfoodfacts
from Database.dbRessources import connect



def FeedCategories():
    queryForCheck = ("SELECT COUNT(*) FROM Category WHERE code=%s")
    queryForInserting = ("INSERT INTO category(code,name,url) VALUES(%s,%s,%s)")
    insertCount = 0
    categories = openfoodfacts.facets.get_categories()
    conn = connect()
    cursor = conn.cursor()

    for category in categories: 
        cursor.execute(queryForInserting, (category['id'],category['name'],category['url']))
        insertCount += 1
        print('category inserted')
        if insertCount == 1000:
            conn.commit()
            insertCount = 0
    cursor.close()
    print("Category feed has been done!")