from abc import ABC


class Category(ABC):
    def __init__(self):
        self.__name = None
        self.__searchList = None
        self.__articleCnt = None

    def make(self):
        pass

    def search_title(self):
        pass

    def search_poject(self):
        pass

    def search_writer(self):
        pass

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


