# Article(추상)

from abc import ABC, abstractmethod


class Article(ABC):
    def __init__(self):
        self._pk = None
        self._title = None
        self._writer = None
        self._comment = None
        self._project = None

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
        return self._pk

    def get_title(self):
        return self._title

    def get_writer(self):
        return self._writer

    def get_comment(self):
        return self._comment

    def get_project(self):
        return self._project

    # Setter

    def set_pk(self, data):
        self._pk = data

    def set_title(self, data):
        self._title = data

    def set_writer(self, data):
        self._writer = data

    def set_comment(self, data):
        self._comment = data

    def set_project(self, data):
        self._project = data

