# Port: Interface for repository
class UserRepositoryInterface:
    def get_user(self, user_id):
        raise NotImplementedError
