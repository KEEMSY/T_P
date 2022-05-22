from abc import ABC, abstractmethod


class Category(ABC):
    def __init__(self):
        self.__name = None
        self.__searchList = None
        self.__articleCnt = None

    @abstractmethod
    def make(self):
        pass

    @abstractmethod
    def search_title(self):
        pass

    @abstractmethod
    def search_project(self):
        pass

    @abstractmethod
    def search_writer(self):
        pass

    @abstractmethod
    def pagination(self):
        pass

    # getter

    def get_name(self):
        return self.__name

    def get_search_list(self):
        return self.__searchList

    def get_article_cnt(self):
        return self.__articleCnt

    # setter

    def set_name(self, data):
        self.__name = data

    def set_search_list(self, data):
        self.__searchList = data

    def set_article_cnt(self, data):
        self.__articleCnt = data


