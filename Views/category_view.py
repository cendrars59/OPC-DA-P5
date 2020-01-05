# -*- coding: Utf-8 -*
# file managing the displays related to the categories

from beautifultable import BeautifulTable


def display_categories_list(cat_list):
    """
    function to display in shell the list of categories
    :param cat_list: list of categories
    """
    table = BeautifulTable()
    table.column_headers = ["id", "name", "URL"]
    table.column_alignments["name"] = BeautifulTable.ALIGN_LEFT
    table.column_alignments["URL"] = BeautifulTable.ALIGN_LEFT
    table.max_table_width = 500
    table.column_widths = [10, 400, 500]
    for cat in cat_list:
        table.append_row([cat[0], cat[2], cat[3]])
    print(table)
    print("""



        """)


def display_category_products(prod_list):
    """
    function to display products belonging to the category
    :param prod_list: product id. Type integer
    """
    table = BeautifulTable()
    table.column_headers = ["id", "name", "URL", "Nutrition score"]
    table.column_alignments["name"] = BeautifulTable.ALIGN_LEFT
    table.column_alignments["URL"] = BeautifulTable.ALIGN_LEFT
    table.max_table_width = 500
    table.column_widths = [10, 400, 500, 20]
    for product in prod_list:
        table.append_row([product[1], product[3], product[5], product[6]])
    print(table)
    print("""
    
    
    
    """)

