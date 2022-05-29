from articleapp.classes.ABC import User


class Supporter(User):
    def __init__(self):
        super(Supporter, self).__init__()

    def change_info(self, data):
        pass

    def change_password(self, data):
        pass


