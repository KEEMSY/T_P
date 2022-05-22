from ABC import User


class Developer(User):
    def __init__(self):
        super(Developer, self).__init__()

    def change_info(self, data):
        pass

    def change_password(self, data):
        pass

    def add_stack(self):
        pass

    def delete_stack(self):
        pass