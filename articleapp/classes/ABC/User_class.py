from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self):
        self._nickname = None
        self._email = None
        self._img = None
        self._bio = None
        self._password = None
        self._pk = None

    @abstractmethod
    def change_info(self, data):
        pass

    @abstractmethod
    def change_password(self, data):
        pass

    # getter

    def get_nickname(self):
        return self._nickname

    def get_email(self):
        return self._email

    def get_img(self):
        return self._img

    def get_bio(self):
        return self._bio

    def get_password(self):
        return self._password

    def get_pk(self):
        return self._pk

    # setter

    def set_nickname(self, data):
        self._nickname = data

    def set_email(self, data):
        self._email = data

    def set_img(self, data):
        self._img = data

    def set_bio(self, data):
        self._nickname = data

    def set_password(self, data):
        self._password = data

    def set_pk(self, data):
        self._pk = data

