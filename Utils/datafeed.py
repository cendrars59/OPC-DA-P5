# -*- coding: Utf-8 -*
import openfoodfacts
from Database.dbRessources import connect
from Utils.Params.feedParams import params


def feed(type,request,table,conn):
    queryForCheck = ("SELECT COUNT(*) FROM {0} WHERE code=%s".format(table))
    queryForInserting = ("INSERT INTO {0} (code,name,url) VALUES(%s,%s,%s)".format(table))
    items_list = request

    for item in items_list:
        cursorCK = conn.cursor()
        cursorCK.execute(queryForCheck,(item['id'],))
        Ckresult = cursorCK.fetchall()
        cursorCK.close() 
        if int(Ckresult[0][0]) == 0:
            cursorIn = conn.cursor()
            cursorIn.execute(queryForInserting, (item['id'],item['name'],item['url']))
            conn.commit()
            cursorIn.close()
            print('{0} inserted'.format(type))
         
    print("{0} feed has been done!".format(type))


def feedDataSet(productId,itemsList,dataSet,refTable,idRefTable,conn):
    for item in itemsList:
        if item != '':
            queryn = ("SELECT {0} FROM {1} WHERE {1}.name = %s".format(idRefTable,refTable))
            cursorn = conn.cursor()
            cursorn.execute(queryn,(item,))
            ids = cursorn.fetchall()
            cursorn.close()
            if len(ids) != 0:
                for Id in ids:
                    dataSet.add((productId,Id[0]))


def insertIntoJunctionTable(dataset,table,dest1,dest2,conn):
    for item in dataset:
        queryI = ("INSERT INTO {0} ({1},{2}) VALUES(%s,%s)".format(table,dest1,dest2)) # Inserting the product into the table
        cursorI = conn.cursor()
        cursorI.execute(queryI, (item[0],item[1]))
        conn.commit()
        cursorI.close()


def feedProducts(conn):

    product_category = set()
    product_brand = set()
    product_store = set()


    query = ("SELECT idCategory,code FROM category WHERE category.is_active=1")  

    cursor = conn.cursor()
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()

    for category in categories:
        # for each category, gathering from Open food facts products
        category_products = openfoodfacts.products.get_by_category(category[1])
        for product in category_products:
        
            # Fitering products having only a valid structure and where the label and id are not empty
            if ('brands'in product and 'stores' in product and 'labels' in product and 'url' in product and 'id' in product
         and product['labels']!='' and product['id'] !=''):

                query1 = ("INSERT INTO product (code,label,url) VALUES(%s,%s,%s)") # Inserting the product into the table
                cursor1 = conn.cursor()
                cursor1.execute(query1, (product['id'],product['labels'],product['url']))
                conn.commit()
                cursor1.close()
            
                query2 = ("SELECT MAX(idProduct) FROM product") # get the product id just inserted into the product table
                cursor2 = conn.cursor()
                cursor2.execute(query2)
                productId = cursor2.fetchall()
                cursor2.close()

                # feeding dataset in order to insert into table product has category 
                product_category.add((productId[0][0],category[0])) 

                # feeding dataset in order to insert into table store has product 
                temp_stores = product['stores'].split(',')
                feedDataSet(productId[0][0],temp_stores,product_store,'store','idStore',conn)
            
                # feeding dataset in order to insert into table brand has product
                temp_brands = product['brands'].split(',')
                feedDataSet(productId[0][0],temp_brands,product_brand,'brand','idBrand',conn)

    # inserting into the junction table 
    insertIntoJunctionTable(product_brand,'Product_has_Brand','Product_idProduct','Brand_idBrand',conn)            
    insertIntoJunctionTable(product_category,'Category_has_Product','Product_idProduct','Category_idCategory',conn)
    insertIntoJunctionTable(product_store,'Product_has_Store','Product_idProduct','Store_idStore',conn)
    




def feedApp():
    conn = connect()
    #feed(params["store"]["type"],params["store"]["request"],params["store"]["table"],conn)
    #feed(params["category"]["type"],params["category"]["request"],params["category"]["table"],conn)
    #feed(params["brand"]["type"],params["brand"]["request"],params["brand"]["table"],conn)
    feedProducts(conn)
