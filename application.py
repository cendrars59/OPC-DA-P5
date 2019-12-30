# -*- coding: Utf-8 -*
from Database.dbRessources import connect
from Database.dbRessources import create_database
from Utils.datafeed import feed_application
from mysql.connector import errorcode
from Models import category
from Models import product
from Views import display


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
        feed_application(connection) 
        print('database creation & feed done')
    list_of_cat = category.get_active_categories(connection)
    list_of_id = []
    for cat in list_of_cat:
        list_of_id.append(str(cat[0]))
    display.display_categories_list(list_of_cat)
    selected = False
    while not selected:
        choice = input('Enter the category id in order to access to the list of products belonging to category:   ')
        if choice in list_of_id:
            selected = True

    cat_products = product.get_products_by_category(connection, int(choice))
    display.display_category_products(cat_products)

    selected = False
    while not selected:
        choice = input('Enter the product id in order to access to the details of a product:   ')
        if choice in list_of_id:
            selected = True


if __name__ == '__main__':
    main()








