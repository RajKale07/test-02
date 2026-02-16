# Presentation Layer: Controllers
from business.services import UserService, ProductService
from presentation.views import display

user_service = UserService()
product_service = ProductService()

def show_user(user):
    name = user_service.get_user_name(user)
    display(f"User Name: {name}")

def show_product(product):
    title = product_service.get_product_title(product)
    display(f"Product Title: {title}")
