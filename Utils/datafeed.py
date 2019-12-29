# -*- coding: Utf-8 -*
import requests
from Utils.Params.feedParams import params


def feed(domain, request, table, conn):
    """
    Generic Function to feed the masters data -> Store , Brand, Category
    conn: object of type connection
    domain : object of type string . type of import
    table : string. destination table
    request : string. API request to gather master data
    """
    print("{0} feed is starting!".format(domain))
    query_for_check = ("SELECT COUNT(*) FROM {0} WHERE code=%s".format(table))
    query_for_inserting = ("INSERT INTO {0} (code, name, url) VALUES(%s,%s,%s)".format(table))
    items_list = request  # Gathering data for api

    for item in items_list:
        cursor_ck = conn.cursor()
        cursor_ck.execute(query_for_check,(item['id'],))
        ckresult = cursor_ck.fetchall()
        cursor_ck.close()
        # if the code doesn't already exit, we can proceed to insert
        if int(ckresult[0][0]) == 0:
            cursor_in = conn.cursor()
            cursor_in.execute(query_for_inserting, (item['id'], item['name'], item['url']))
            conn.commit()
            cursor_in.close()

    print("{0} feed has been done!".format(domain))


def feed_data_set(product_id, items_list, data_set, ref_table, id_ref_table, conn):
    """
    Generic Function to feed the data set used for feed the junction table
    conn: object of type connection
    data_set : object of type set
    table : string destination table
    dest 1 & 1 : string fields to insert
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
    Generic Function to feed the junction tables
    conn: object of type connection
    data_set : object of type set
    table : string destination table
    dest 1 & 1 : string fields to insert
    """
    for item in data_set:
        query_i = ("INSERT INTO {0} ({1},{2}) VALUES(%s,%s)".format(table, dest1, dest2))  # Inserting into the table
        cursor_i = conn.cursor()
        cursor_i.execute(query_i, (item[0], item[1]))
        conn.commit()
        cursor_i.close()


def feed_products(conn):
    """
    Function to feed the products into the database according the category
    conn: object of type connection
    """

    product_category = set()
    product_brand = set()
    product_store = set()

    # Gathering active categories into DB.
    query = "SELECT idCategory, code, name FROM category WHERE is_active = 1"

    cursor = conn.cursor()
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    print("The products loading will be performed for {0} active categories".format(str(len(categories))))
    print("products loading is starting. It could take a while...Have a break :-) ")
    for category in categories:
        print('loading products for the category : {}'.format(category[2]))
        payload = {
            "search_terms2": category[2],
            "search_tag": "categories",
            "sort_by": "unique_scans_n",
            "page": 1,
            "page_size": 1000,
            "action": "process",
            "json": 1}
        # API request to gather products according the given payload
        response = requests.get(params['product']['url'], params=payload, headers=params['product']['headers'])
        products = response.json()

        # for each active category, gathering from Open food facts products
        for product in products['products']:

            # verify if the product already exists into the database the search is by open fact food id <-> code into db
            if 'id' in product:
            
                query_for_check = ("SELECT COUNT(*) FROM {0} WHERE code={1}".format('product', product['id']))
                cursor_ck = conn.cursor()
                cursor_ck.execute(query_for_check)
                ckresult = cursor_ck.fetchall()
                cursor_ck.close()
                # Filtering products having only a valid structure and where the label and id are not empty and 
                # the product doesn't exist into the database.
                if ('brands' in product and 'stores' in product and 'product_name' in product and 'url' in product and
                        product['product_name'] != '' and product['id'] != '' and ckresult[0][0] == 0):

                    query1 = "INSERT INTO product (code,label,url) VALUES(%s,%s,%s)" # Inserting the product
                    cursor1 = conn.cursor()
                    cursor1.execute(query1, (product['id'], product['product_name'], product['url']))
                    conn.commit()
                    cursor1.close()

                    # get the product id just inserted
                    query2 = ("SELECT MAX(idProduct) FROM product where code = {0}".format(product['id']))
                    cursor2 = conn.cursor()
                    cursor2.execute(query2)
                    product_id = cursor2.fetchall()
                    cursor2.close()
                    print(product_id[0][0])

                    # feeding dataset in order to insert into table product has category
                    product_category.add((product_id[0][0], category[0]))
                    print(product_category)

                    # feeding dataset in order to insert into table store has product
                    temp_stores = product['stores'].split(',')
                    feed_data_set(product_id[0][0], temp_stores, product_store, 'store', 'idStore', conn)
                    print(product_store)

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
    Function to feed the database :
    - Category
    - Product
    - Store
    - Brand
    - and the junction tables
    conn: object of type connection
    """
    #feed(params["store"]["type"], requests.get(params["store"]["url"]).json()['tags'], params["store"]["table"], conn)
    #feed(params["brand"]["type"], requests.get(params["brand"]["url"]).json()['tags'], params["brand"]["table"], conn)
    #feed(params["category"]["type"], requests.get(params["category"]["url"]).json()['tags'], params["category"]["table"], conn)
    feed_products(conn)
