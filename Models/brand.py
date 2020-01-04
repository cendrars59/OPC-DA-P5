from Database.getDataFromDb import get_product_brands


class Brand:

    def __init__(self, id, code, label, url, is_active):
        """
        Function to create brand object
        """
        self.id = id
        self.code = code
        self.label = label
        self.url = url
        self.activated = is_active

    @classmethod
    def get_brands_by_product(cls, conn, id):
        """
        Function to get the brands information according a given product
        """

        products_data = get_product_brands(conn, id)
        product_brands = []
        for data in products_data:
            brand = Brand(data["id"], data["code"], data["label"], data["url"], data["is_active"])
            product_brands.append(brand)
        return product_brands
