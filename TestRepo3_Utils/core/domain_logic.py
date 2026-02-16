# Core domain logic (independent)
class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def get_user_name(self, user_id):
        user = self.user_repo.get_user(user_id)
        if user:
            return user['name']
        return None
