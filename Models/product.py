from Database.getDataFromDb import get_products_by_category


class Product:

    def __init__(self, id, code, label, url, is_active, ingredients_text, nutrition_grade_fr, quantity,
                 list_brands=None, list_stores=None):
        """
        Function to create product object
        """
        self.id = id
        self.code = code
        self.label = label
        self.url = url
        self.activated = is_active
        self.ingredients = ingredients_text
        self.nutrition_grade = nutrition_grade_fr
        self.qty = quantity
        self.brands = list_brands
        self.stores = list_stores

    @classmethod
    def get_products_by_cat(cls, conn, category):
        """
        Function to get the products information according a given category
        """

        products_data = get_products_by_category(conn, category.id)
        product_list = []
        for data in products_data:
            product = Product(data["id"], data["code"], data["label"], data["url"], data["is_active"],
                              data["ingredients_text"], data["nutrition_grade_fr"], data["quantity"])

            product_list.append(product)
        return product_list
