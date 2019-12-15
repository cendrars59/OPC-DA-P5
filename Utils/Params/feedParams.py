# -*- coding: Utf-8 -*
import openfoodfacts

params = {
  'store' : {

  'type': 'store',
  'table': 'store',
  'request':openfoodfacts.facets.get_stores(),
  },

  'category': {

    'type': 'category',
    'table': 'category',
    'request':openfoodfacts.facets.get_categories(),
  },

  'brand': {

    'type': 'brand',
    'table': 'brand',
    'request':openfoodfacts.facets.get_brands(),
  },

}
