from abc import ABC


class User(ABC):
    def __init__(self):
        self.__nickname = None
        self.__email = None
        self.__img = None
        self.__bio = None
        self.__password = None

    def change_info(self, data):
        pass

    def change_password(self, data):
        pass

    # getter

    def get_nickname(self):
        return self.__nickname

    def get_email(self):
        return self.__email

    def get_img(self):
        return self.__img

    def get_bio(self):
        return self.__bio

    def get_password(self):
        return self.__password

    # setter

    def set_nickname(self, data):
        self.__nickname = data

    def set_email(self, data):
        self.__email = data

    def set_img(self, data):
        self.__img = data

    def set_bio(self, data):
        self.__nickname = data

    def set_password(self, data):
        self.__password = data

