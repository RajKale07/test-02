# Simple Event Driven Example
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, handler):
        self.subscribers.setdefault(event, []).append(handler)

    def publish(self, event, data):
        for handler in self.subscribers.get(event, []):
            handler(data)

# Handlers
def handle_order(order):
    print(f"Processing order: {order}")

def handle_email(email):
    print(f"Sending email to: {email}")

# Demo
bus = EventBus()
bus.subscribe("order_placed", handle_order)
bus.subscribe("order_placed", handle_email)

bus.publish("order_placed", {"order_id": 101, "customer": "Raj"})
