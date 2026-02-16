# Sample data model
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def sample_products():
    return [Product("Laptop", 1000), Product("Mouse", 50)]
