
# Project(추상)
from abc import ABC, abstractmethod


class Project(ABC):
    def __init__(self):
        self._leader = None
        self._team = None
        self._stack = None
        self._title = None
        self._due_date = None
        self._desc = None
        self._tool = None

    @abstractmethod
    def make_project(self, title, leader, stack, due_date, desc, tool):
        pass

    @abstractmethod
    def delete_project(self):
        pass

    @abstractmethod
    def update_project(self):
        pass

    @abstractmethod
    def see_now(self):
        pass

    # Getter 설정

    def get_leader(self):
        return self._leader

    def get_team(self):
        return self._team

    def get_stack(self):
        return self._stack

    def get_title(self):
        return self._title

    def get_due_date(self):
        return self._due_date

    def get_desc(self):
        return self._desc

    def get_tool(self):
        return self._tool

    # Setter 설정

    def set_leader(self, data):
        self._leader = data

    def set_team(self, data):
        self._team = data

    def set_stack(self, data):
        self._stack = data

    def set_title(self, data):
        self._title = data

    def set_due_date(self, data):
        self._due_date = data

    def set_desc(self, data):
        self._desc = data

    def set_tool(self, data):
        self._tool = data



