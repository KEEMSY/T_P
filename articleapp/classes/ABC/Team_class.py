from abc import ABC, abstractmethod


class Team(ABC):
    def __int__(self):
        self.__teamList = []
        self.__leader = None
        self.__supporterList = []

    @abstractmethod
    def make_team(self):
        pass

    @abstractmethod
    def append_team(self):
        pass

    @abstractmethod
    def delete_team(self):
        pass
