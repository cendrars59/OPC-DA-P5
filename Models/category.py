from Database.getDataFromDb import get_active_categories

class Category:

    def __init__(self, id, code, label, url):
        """
        Function to create category object
        :param id: type int . category id into db
        :param code: type string .
        :param label: type string .
        :param url: type string .
        """

        self.id = id
        self.code = code
        self.label = label
        self.url = url
        self.products_category = None

    @classmethod
    def get_active_categories(cls, conn):
        """
        Function to gather the active categories
        :param conn: Object of type connection
        """
        active_category_list = []
        gathered_data = get_active_categories(conn)
        for data in gathered_data:
            category = Category(data['id'], data['code'], data['name'], data['url'])
            active_category_list.append(category)

