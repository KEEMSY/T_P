from abc import ABC, abstractmethod


class Category(ABC):
    def __init__(self):
        self._name = None
        self._searchList = None
        self._articleCnt = None

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
        return self._name

    def get_search_list(self):
        return self._searchList

    def get_article_cnt(self):
        return self._articleCnt

    # setter

    def set_name(self, data):
        self._name = data

    def set_search_list(self, data):
        self._searchList = data

    def set_article_cnt(self, data):
        self._articleCnt = data


