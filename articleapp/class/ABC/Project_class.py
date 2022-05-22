
# Project(추상)
from abc import ABC, abstractmethod


class Project(ABC):
    def __init__(self):
        self.__leader = None
        self.__team = None
        self.__stack = None
        self.__title = None
        self.__due_date = None
        self.__desc = None
        self.__tool = None

    def make_project(self, title, leader, stack, due_date, desc, tool):
        self.set_title(title)
        self.set_leader(leader)
        self.set_stack(stack)
        self.set_due_date(due_date)
        self.set_desc(desc)
        self.set_tool(tool)

    # Getter 설정

    def get_leader(self):
        return self.__leader

    def get_team(self):
        return self.__team

    def get_stack(self):
        return self.__stack

    def get_title(self):
        return self.__title

    def get_due_date(self):
        return self.__due_date

    def get_desc(self):
        return self.__desc

    def get_tool(self):
        return self.__tool

    # Setter 설정

    def set_leader(self, data):
        self.__leader = data

    def set_team(self, data):
        self.__team = data

    def set_stack(self, data):
        self.__stack = data

    def set_title(self, data):
        self.__title = data

    def set_due_date(self, data):
        self.__due_date = data

    def set_desc(self, data):
        self.__desc = data

    def set_tool(self, data):
        self.__tool = data



