# -*- coding: Utf-8 -*
# Package in order to manage
# - the connection to the database and gathering data according different kinds of requests

import mysql.connector
from os import system
from mysql.connector import errorcode


def get_active_categories(conn):
    """
    function to retrieve the active categories
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM category WHERE is_active = 1')
    active_categories = cursor.fetchall()
    cursor.close()
    return active_categories


def get_products_by_category(conn, category_id):
    """
    function to retrieve the products according a given category
    """
    query = """
    SELECT
       name as category_name,
       P.idProduct,
       P.code,
       P.label,
       P.is_active,
       P.url,
       P.nutrition_grade_fr,
       P.quantity

    FROM category_has_product
        INNER JOIN Category C ON Category_has_Product.Category_idCategory = C.idCategory
        INNER JOIN Product P ON Category_has_Product.Product_idProduct = P.idProduct

        WHERE Category_idCategory = {0}
    
    
    """.format(category_id)
    cursor = conn.cursor()
    cursor.execute(query)
    products_data = cursor.fetchall()
    cursor.close()
    return products_data
