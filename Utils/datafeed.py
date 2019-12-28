# -*- coding: Utf-8 -*
import requests
import json
from Database.dbRessources import connect
from Utils.Params.feedParams import params



def feed(domain, request,table, conn):
    """

    """
    print("{0} feed is starting!".format(domain))
    query_for_check = ("SELECT COUNT(*) FROM {0} WHERE code=%s".format(table))
    query_for_inserting = ("INSERT INTO {0} (code, name, url) VALUES(%s,%s,%s)".format(table))
    items_list = request  #Gathering data for api 
    
    
    for item in items_list:
        cursor_ck = conn.cursor()
        cursor_ck.execute(query_for_check,(item['id'],))
        ckresult = cursor_ck.fetchall()
        cursor_ck.close()
        #if the code doesn't already exit, we can proceed to the insert
        if int(ckresult[0][0]) == 0:
            cursor_in = conn.cursor()
            cursor_in.execute(query_for_inserting, (item['id'], item['name'], item['url']))
            conn.commit()
            cursor_in.close()
            print('{0} inserted'.format(domain))
         
    print("{0} feed has been done!".format(domain))


def feed_data_set(product_id, items_list, data_set, ref_table, id_ref_table, conn):
    """

    """
    for item in items_list:
        if item != '':
            query_n = ("SELECT {0} FROM {1} WHERE {1}.name = %s".format(id_ref_table, ref_table))
            cursor_n = conn.cursor()
            cursor_n.execute(query_n, (item,))
            ids = cursor_n.fetchall()
            cursor_n.close()
            if len(ids) != 0:
                for Id in ids:
                    data_set.add((product_id, Id[0]))


def insert_into_junction(data_set, table, dest1, dest2, conn):
    """

    """
    for item in data_set:
        query_i = ("INSERT INTO {0} ({1},{2}) VALUES(%s,%s)".format(table, dest1, dest2))  # Inserting into the table
        cursor_i = conn.cursor()
        cursor_i.execute(query_i, (item[0], item[1]))
        conn.commit()
        cursor_i.close()


def feed_products(conn):
    """

    """
   
    
    product_category = set()
    product_brand = set()
    product_store = set()

    #Gathering active categories into DB. 
    query = ("SELECT idCategory,code,name FROM category WHERE category.is_active=1")  

    cursor = conn.cursor()
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    print("The products loading will be performed for {0} active categories".format(str(len(categories))))
    print("products loading is starting. It could take a while...Have a break :-) ")
    for category in categories:
        
        payload = {'categories': category[1], 'json': 1, 'page_size' : '1000'}
        response = requests.get(url = params['product']['url'], headers=params['product']['headers'], params = payload)

        products=response.json()
       
        
        # for each active category, gathering from Open food facts products
        for product in products['products']:
            # Filtering products having only a valid structure and where the label and id are not empty
            if ('brands' in product and 'stores' in product and 'product_name' in product and 'url' in product and
                    'id' in product and product['product_name'] != '' and product['id'] != ''):

                
                query1 = ("INSERT INTO product (code,label,url) VALUES(%s,%s,%s)") # Inserting the product
                cursor1 = conn.cursor()
                cursor1.execute(query1, (product['id'], product['product_name'], product['url']))
                conn.commit()
                cursor1.close()
            
                query2 = ("SELECT MAX(idProduct) FROM product")  # get the product id just inserted
                cursor2 = conn.cursor()
                cursor2.execute(query2)
                product_id = cursor2.fetchall()
                cursor2.close()

                # feeding dataset in order to insert into table product has category 
                product_category.add((product_id[0][0], category[0]))

                # feeding dataset in order to insert into table store has product 
                temp_stores = product['stores'].split(',')
                feed_data_set(product_id[0][0], temp_stores, product_store, 'store', 'idStore', conn)
            
                # feeding dataset in order to insert into table brand has product
                temp_brands = product['brands'].split(',')
                feed_data_set(product_id[0][0], temp_brands, product_brand, 'brand', 'idBrand', conn)

    # inserting into the junction table 
    insert_into_junction(product_brand, 'Product_has_Brand', 'Product_idProduct', 'Brand_idBrand', conn)
    insert_into_junction(product_category, 'Category_has_Product', 'Product_idProduct', 'Category_idCategory', conn)
    insert_into_junction(product_store, 'Product_has_Store', 'Product_idProduct', 'Store_idStore', conn)

    print("Products loading is finished")
    

def feed_application(conn):
    """

    """
    feed(params["store"]["type"], requests.get(params["store"]["url"]).json()['tags'], params["store"]["table"], conn)
    feed(params["brand"]["type"], requests.get(params["brand"]["url"]).json()['tags'], params["brand"]["table"], conn)
    feed(params["category"]["type"], requests.get(params["category"]["url"]).json()['tags'], params["category"]["table"], conn)
    #feed_products(conn)
