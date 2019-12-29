# -*- coding: Utf-8 -*
# Required parameters to perform the feeding of th database

params = {
    'store': {

        'type': 'store',
        'table': 'store',
        'url': 'https://fr.openfoodfacts.org/products/stores.json'
    },

    'category': {

        'type': 'category',
        'table': 'category',
        'url': 'https://fr.openfoodfacts.org/products/categories.json'
    },

    'brand': {

        'type': 'brand',
        'table': 'brand',
        'url': 'https://fr.openfoodfacts.org/products/brands.json'
    },

    'product': {

        'type': 'product',
        'table': 'product',
        'url': 'https://fr.openfoodfacts.org/cgi/search.pl?',
        'headers': {'User-Agent': 'Cyril-59, Mozilla, Version 1.0'},
    }

    

}
