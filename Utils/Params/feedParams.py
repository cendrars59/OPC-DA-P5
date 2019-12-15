# -*- coding: Utf-8 -*
import openfoodfacts

params = {
  'store' : {

  'type': 'store',
  'table': 'store',
  'request':openfoodfacts.facets.get_stores(),}  
}
