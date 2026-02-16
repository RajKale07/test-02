# MVC Example

# Model
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

# View
def render_user(user):
    print(f"User Info -> ID: {user.user_id}, Name: {user.name}")

# Controller
class UserController:
    def __init__(self, user):
        self.user = user

    def show(self):
        render_user(self.user)

# Usage
if __name__ == "__main__":
    user = User(1, "Raj")
    controller = UserController(user)
    controller.show()
