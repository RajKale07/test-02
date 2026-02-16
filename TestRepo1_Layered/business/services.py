# Business Layer: Services
from data.models import User, Product

class UserService:
    def get_user_name(self, user):
        return user.name

class ProductService:
    def get_product_title(self, product):
        return product.title
