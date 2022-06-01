from abc import ABC, abstractmethod


class Team(ABC):
    def __init__(self):
        self._developerList = None
        self._leader = None
        self._supporterList = None

    @abstractmethod
    def make_team(self, data):
        pass

    @abstractmethod
    def append_developer(self, data):
        pass

    @abstractmethod
    def delete_developer(self, data):
        pass

    @abstractmethod
    def register_leader(self, data):
        pass

    @abstractmethod
    def append_supporter(self, data):
        pass

    @abstractmethod
    def delete_supporter(self, data):
        pass

    # getter
    def get_team_list(self):
        return self._developerList

    def get_leader(self):
        return self._leader

    def get_supporter_list(self):
        return self._supporterList

    # setter
    def set_team_list(self, data):
        self._developerList = data
        return True

    def set_leader(self, data):
        self._leader = data

    def set_supporter_list(self, data):
        self._supporterList = data


