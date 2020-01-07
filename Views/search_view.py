# -*- coding: Utf-8 -*
# file managing the displays related to the categories

from beautifultable import BeautifulTable


def display_search(search_list):
    """
    function to display products belonging to the category
    :param search_list: product id. Type integer
    """
    table = BeautifulTable()
    table.column_headers = ["user", "category", "product", "date"]
    table.column_alignments["user"] = BeautifulTable.ALIGN_LEFT
    table.column_alignments["category"] = BeautifulTable.ALIGN_LEFT
    table.column_alignments["product"] = BeautifulTable.ALIGN_LEFT
    table.max_table_width = 500
    table.column_widths = [10, 400, 500, 20]
    for search in search_list:
        table.append_row([search[2], search[1], search[0], search[3]])
    print(table)
    print("""



    """)
