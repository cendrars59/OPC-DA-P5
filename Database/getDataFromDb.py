# -*- coding: Utf-8 -*
# Package in order to manage
# - the connection to the database and gathering data according different kinds of requests


def get_active_categories(conn):
    """
    function to retrieve the active categories
    :param conn: DB connection type
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM category WHERE is_active = 1')
    active_categories = cursor.fetchall()
    cursor.close()
    return active_categories


def get_products_by_category(conn, category_id):
    """
    function to retrieve the products according a given category
    :param conn: DB connection type
    :param category_id: category id. Type integer
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


def get_product_stores(conn, prod_id):
    """
    function to retrieve the stores associated to a product
    :param conn: DB connection type
    :param prod_id: product id. Type integer
    """
    query = """
    SELECT
       s.code,
       s.name,
       s.url
    FROM product_has_store
        INNER JOIN store s ON product_has_store.Store_idStore = s.idStore
    WHERE product_has_store.Product_idProduct = {0}
    """.format(prod_id)

    cursor = conn.cursor()
    cursor.execute(query)
    products_stores = cursor.fetchall()
    cursor.close()
    return products_stores


def get_product_brands(conn, prod_id):
    """
    function to retrieve the brands associated to a product
    :param conn: DB connection type
    :param prod_id: product id. Type integer
    """
    query = """
    SELECT
       b.code,
       b.name,
       b.url
    FROM product_has_brand
        INNER JOIN brand b ON product_has_brand.Brand_idBrand = b.idBrand
    WHERE product_has_brand.Product_idProduct = {0}
    """.format(prod_id)

    cursor = conn.cursor()
    cursor.execute(query)
    product_brands = cursor.fetchall()
    cursor.close()
    return product_brands


def get_product(conn, prod_id):
    """
    function to retrieve the brands associated to a product
    :param conn: DB connection type
    :param prod_id: product id. Type integer
    """
    query = """
       SELECT
            p.idProduct,
            p.code,
            p.label,
            p.url,
            p.is_active,
            p.ingredients_text,
            p.nutrition_grade_fr,
            p.quantity

        FROM product p
        WHERE idProduct = {0}
        """.format(prod_id)

    cursor = conn.cursor()
    cursor.execute(query)
    product = cursor.fetchall()
    cursor.close()
    return product


def get_nutrition_grade_by_category(conn, cat_id):
    """
    function to retrieve the existing grades for a given category
    :param conn: DB connection type
    :param cat_id: category id. Type integer

    """
    query = """
    SELECT
        DISTINCT nutrition_grade_fr
    FROM category_has_product
        INNER JOIN product p on category_has_product.Product_idProduct = p.idProduct
    WHERE Category_idCategory = {0}
    ORDER BY nutrition_grade_fr ASC
    """.format(cat_id)

    cursor = conn.cursor()
    cursor.execute(query)
    nutrition_grades = cursor.fetchall()
    cursor.close()
    return nutrition_grades


def get_products_by_nut_grade_and_cat(conn, cat_id, grades_list):
    """
     function to retrieve the products according a nutrition range
     :param conn: DB connection type
     :param cat_id: category id. Type integer
     :param grades_list: list of distinct nutrition grades. Type list of strings
    """
    query = """
    SELECT
        p.idProduct,
        p.label,
        p.url,
        p.nutrition_grade_fr
    FROM category_has_product
        INNER JOIN product p on category_has_product.Product_idProduct = p.idProduct
    WHERE Category_idCategory = {0} and p.nutrition_grade_fr IN {1}
    ORDER BY p.nutrition_grade_fr ASC
    """.format(cat_id, grades_list)

    cursor = conn.cursor()
    cursor.execute(query)
    nutrition_grades = cursor.fetchall()
    cursor.close()
    return nutrition_grades


def get_user(conn, login):
    """
    function to verify if the user exists into the DB.
    :param conn: DB connection type
    :param login: user login. Type string
    """
    query = "SELECT name FROM user WHERE name = %s"
    cursor = conn.cursor()
    cursor.execute(query, (login,))
    user = cursor.fetchall()
    cursor.close()
    return user

def create_user(conn, login):
    """
        function to verify if the user exists into the DB.
        :param conn: DB connection type
        :param login: user login. Type string
        """
    query = "INSERT INTO user (name) values (%s)"
    cursor = conn.cursor()
    cursor.execute(query, (login,))
    conn.commit()
    cursor.close()





