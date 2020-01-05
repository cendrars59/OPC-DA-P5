# -*- coding: Utf-8 -*
from Database.dbRessources import connect
from Database.dbRessources import create_database
from Database.getDataFromDb import *
from Utils.datafeed import feed_application
from mysql.connector import errorcode
from Models import category
from Models import product
from Models.product import Product
from Models import brand
from Models import store
from Views import category_view
from Views import product_view


def main():
    # Access to database to access to the data
    connection = connect()
    
    if connection == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check database credential")
    # If the database does'nt exist it is created and feed
    elif connection == errorcode.ER_BAD_DB_ERROR:
        print('Database is not created')
        print('Database will be created and data inserted')
        print('it will take a while. Have a break')
        create_database()
        connection = connect()
        feed_application(connection) 
        print('database creation & feed done')

    # Display of the list of categories

    list_of_cat = category.get_active_categories(connection)
    list_of_id = []
    for cat in list_of_cat:
        list_of_id.append(str(cat[0]))
    category_view.display_categories_list(list_of_cat)
    selected = False
    while not selected:
        choice = input('Enter the category id in order to access to the list of products belonging to category:   ')
        if choice in list_of_id:
            selected = True

    # Display the list of products belonging to a category
    list_of_grades = get_nutrition_grade_by_category(connection, choice)
    grades = []
    for grade in list_of_grades:
        grades.append(grade[0])

    cat_products = product.get_products_by_category(connection, int(choice))
    list_of_products_id = []
    for prod in cat_products:
        list_of_products_id.append(str(prod[1]))
    category_view.display_category_products(cat_products)

    selected = False
    while not selected:
        product_choice = input('Enter the product id in order to access to the details of a product:  ')
        if product_choice in list_of_products_id:
            selected = True




    # Display of the detailed view

    selection = get_product(connection, product_choice)
    selected_product = Product(id=selection[0][0], code=selection[0][1], label=selection[0][2], url=selection[0][3],
                               is_active=selection[0][4], ingredients_text=selection[0][5],
                               nutrition_grade_fr=selection[0][6], quantity=selection[0][7])
    selected_product.stores = store.get_product_stores(connection, product_choice)
    selected_product.brands = brand.get_product_brands(connection, product_choice)

    product_range = grades.index(selected_product.nutrition_grade)

    if product_range == 0:
        print( "('{0}')".format(selected_product.nutrition_grade))
        recommended_products = get_products_by_nut_grade_and_cat(connection, choice,
                                                                 "('{0}')".format(selected_product.nutrition_grade))

    else:
        list1 = str(grades[0:product_range]).replace("[", "(")
        list2 = list1.replace("]", ")")
        recommended_products = get_products_by_nut_grade_and_cat(connection, choice, list2)

    product_view.display_detailed_product(selected_product, recommended_products)



if __name__ == '__main__':
    main()








