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
    view_categories = False
    view_products = False
    view_detail = False
    view_search = False
    is_running = True

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
    user = None
    credential_validated = False
    who = input('Are you a known user ? Type y for Yes or n for No ')
    if who == 'y':
        login_exist = False
        while not login_exist:
            login = input('enter your login ').lower()
            user = get_user(connection, login)
            if len(user) == 1:
                print('login successful')
                credential_validated = True
                login_exist = True
            else:
                print("user doesn't exist")
    elif who == 'n':
        login_created = False
        while not login_created:
            login = input('enter a new login ').lower()
            user = get_user(connection, login)
            if len(user) == 0:
                create_user(connection,login)
                print('user created')
                credential_validated = True
                login_created = True
            else:
                print('user already exists, choose an other login')

    while is_running:

        menu_selection = input("""
        enter se to access to the search history 
        enter c to access to the category
        """)

        if menu_selection == 'c':
            view_categories = True

        # Display of the list of categories
        if view_categories:
            list_of_cat = category.get_active_categories(connection)
            list_of_id = []
            for cat in list_of_cat:
                list_of_id.append(str(cat[0]))
            category_view.display_categories_list(list_of_cat)
            selected = False
            while not selected:
                choice = input('Enter the category id in order to access to the list of products belonging'
                               ' to category:   ')
                if choice in list_of_id:
                    selected = True
                    view_categories = False
                    view_products = True

        if view_products:
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
                product_choice = input('Enter the product id in order to access to the details of'
                                       ' a product or enter c to go to the categories page:  ')
                if product_choice == 'c':
                    view_products = False
                    view_categories = True
                    selected = True
                elif product_choice in list_of_products_id:
                    selected = True
                    view_products = False
                    view_detail = True

            if view_detail:
                # Display of the detailed view
                selection = get_product(connection, product_choice)  # Get all information for the product from DB
                selected_product = Product(id=selection[0][0], code=selection[0][1], label=selection[0][2],
                                           url=selection[0][3], is_active=selection[0][4],
                                           ingredients_text=selection[0][5], nutrition_grade_fr=selection[0][6],
                                           quantity=selection[0][7])
                selected_product.stores = store.get_product_stores(connection, product_choice)  # Get the list of stores
                selected_product.brands = brand.get_product_brands(connection, product_choice)  # Get the list of brands

                # get ranking of the product according the range of grades
                product_ranking = grades.index(selected_product.nutrition_grade)

                # In case the product has the best ranking
                if product_ranking == 0:
                    print("('{0}')".format(selected_product.nutrition_grade))
                    recommended_products = get_products_by_nut_grade_and_cat(connection, choice, "('{0}')".format(
                        selected_product.nutrition_grade))

                else:
                    recommended_products = get_products_by_nut_grade_and_cat(connection, choice,
                                                                             str(grades[0:product_ranking]).replace("[", "(").replace("]", ")"))

                product_view.display_detailed_product(selected_product, recommended_products)

                ended = False
                while not ended:
                    decision = input(
                        'Type f to finish or l to go to the products or c to go to the categories or s to save:  ')
                    if decision == 'c':
                        view_products = False
                        view_categories = True
                        view_detail = False
                        ended = True
                    elif decision == 'l':
                        view_products = True
                        view_categories = False
                        view_detail = False
                        ended = True
                    elif decision == 'f':
                        is_running = False
                        ended = True
                    elif decision == 's':
                        create_user_search(connection, choice, product_choice, user[0][0])


if __name__ == '__main__':
    main()








