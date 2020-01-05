from Database.getDataFromDb import get_product_stores


class Store:

    def __init__(self, id, code, label, url, is_active):
        """
        Function to create store object
        :param id: Type integer
        :param code: Type string
        :param label: Type string
        :param url: Type string
        :is_active: Type integer
        """

        self.id = id
        self.code = code
        self.label = label
        self.url = url
        self.activated = is_active

    @classmethod
    def get_stores_by_product(cls, conn, id):
        """
        Function to get the brands information according a given product
        :param conn: Object of type connection
        :param id: id of the product. Type integer
        """

        products_data = get_product_stores(conn, id)
        product_stores = []
        for data in products_data:
            store = Store(data["id"], data["code"], data["label"], data["url"], data["is_active"])
            product_stores.append(store)
        return product_stores
