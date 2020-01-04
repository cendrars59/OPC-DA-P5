def display_detailed_product(product):
    """
    Function to display the detailed view of a product
    taking as argument
    product : type product

    """

    print("""
    ----------------------------------------------------------------------------------------------
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