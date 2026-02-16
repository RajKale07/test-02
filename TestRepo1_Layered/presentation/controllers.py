from business.services import calculate_total, apply_discount
from data.models import sample_products

def main_controller():
    products = sample_products()
    prices = [p.price for p in products]
    total = calculate_total(prices)
    discounted = apply_discount(total)
    print(f"Total: {total}, Discounted: {discounted}")

if __name__ == "__main__":
    main_controller()
