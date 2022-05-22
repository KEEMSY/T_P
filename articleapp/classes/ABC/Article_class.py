# Article(추상)

from abc import ABC, abstractmethod


class Article(ABC):
    def __init__(self):
        self.__pk = None
        self.__title = None
        self.__writer = None
        self.__comment = None
        self.__project = None

    # Abstractmethod
    @abstractmethod
    def like(self):
        pass

    @abstractmethod
    def unlike(self):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def contact(self):
        pass

    @abstractmethod
    def make(self):
        pass

    # Getter

    def get_pk(self):
        return self.__pk

    def get_title(self):
        return self.__title

    def get_writer(self):
        return self.__writer

    def get_comment(self):
        return self.__comment

    def get_project(self):
        return self.__project

    # Setter

    def set_pk(self, data):
        self.__pk = data

    def set_title(self, data):
        self.__title = data

    def set_writer(self, data):
        self.__writer = data

    def set_comment(self, data):
        self.__comment = data

    def set_project(self, data):
        self.__project = data

