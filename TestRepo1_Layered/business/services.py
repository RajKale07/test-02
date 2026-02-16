# Sample service for Layered Architecture
def calculate_total(prices):
    return sum(prices)

def apply_discount(total, discount=0.1):
    return total * (1 - discount)
