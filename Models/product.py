from Database.getDataFromDb import get_products_by_category


class Product:

    def __init__(self, id, code, label, url, is_active, ingredients_text, nutrition_grade_fr, quantity,
                 list_brands=None, list_stores=None):
        """
        Function to create product object
        :param id: Type integer
        :param code: Type string
        :param label: Type string
        :param url: Type string
        :param is_active: Type integer
        :param ingredients_text: Type string
        :param nutrition_grade_fr: Type string
        :param quantity: Type string
        :param list_brands: Type list
        :param list_stores: Type list
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
        :param conn: Object of type connection
        :param category: category. Type category
        """

        products_data = get_products_by_category(conn, category.id)
        product_list = []
        for data in products_data:
            product = Product(data["id"], data["code"], data["label"], data["url"], data["is_active"],
                              data["ingredients_text"], data["nutrition_grade_fr"], data["quantity"])

            product_list.append(product)
        return product_list
