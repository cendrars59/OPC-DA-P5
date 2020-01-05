# -*- coding: Utf-8 -*
# file managing the displays related to the products

def display_detailed_product(product, recommanded_products):
    """
    Function to display the detailed view of a product
    :param product: product. Type product
    :param recommanded_products: list of products
    """

    print("""
    -------------------------------------------------------------------------------------------------------------------
    ------------------------------------------- Product detailed view -------------------------------------------------
    id : {0}
    code : {1}
    label : {2}
    ingredients : {3}
    quantity : {4}
    nutrition grade : {5}
    link : {6}
    -----------------------------------------------------Stores--------------------------------------------------------
    available in : 
    """.format(product.id, product.code, product.label, product.ingredients, product.qty,
                product.nutrition_grade, product.url))

    if len(product.stores) == 0:
        print("""
        Not available in stores
        """)
    else:
        for store in product.stores:
            print("""- store : {0} -> link : {1} """.format(store[1], store[2]))

    print("""
    --------------------------------------------------Brands------------------------------------------------------------
    
    """)

    if len(product.brands) == 0:
        print("""
        No brand
        """)
    else:
        for brand in product.brands:
            print("""- brand : {0} -> link : {1}""".format(brand[1], brand[2]))

    print("""
        --------------------------------------------Recommanded products-----------------------------------------------

        """)

    for product in recommanded_products:
        print(""" id : {0} | nutrition score : {3}  | label : {1} | url : {2}     """.format(product[0], product[1],
                                                                                             product[2], product[3]))

    print("""
    
    
    
    """)
