from abc import ABC


class Team(ABC):
    def __int__(self):
        self.__teamList = []
        self.__leader = None
        self.__supporterList = []

    def make_team(self):
        pass

    def append_team(self):
        pass

    def delete_team(self):
        pass
