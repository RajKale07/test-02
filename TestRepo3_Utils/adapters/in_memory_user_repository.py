# Adapter: In-memory implementation of repository
from ports.user_repository_interface import UserRepositoryInterface

class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = {
            1: {"name": "Raj"},
            2: {"name": "Nihar"}
        }

    def get_user(self, user_id):
        return self.users.get(user_id)

# Usage
if __name__ == "__main__":
    repo = InMemoryUserRepository()
    service = UserService(repo)
    print(service.get_user_name(1))  # Output: Raj
