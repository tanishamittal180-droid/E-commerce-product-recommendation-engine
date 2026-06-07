# src/product.py

class Product:

    def __init__(
            self,
            product_id,
            name,
            category,
            price,
            rating):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating