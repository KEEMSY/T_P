from abc import ABC, abstractmethod


class Team(ABC):
    def __int__(self):
        self._teamList = None
        self._leader = None
        self._supporterList = None

    @abstractmethod
    def make_team(self, data):
        pass

    @abstractmethod
    def append_member(self, data):
        pass

    @abstractmethod
    def delete_member(self, data):
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
        return self._teamList

    def get_leader(self):
        return self._leader

    def get_supporter_list(self):
        return self._supporterList

    # setter
    def set_team_list(self, data):
        self._teamList = data

    def set_leader(self, data):
        self._leader = data

    def set_supporter(self, data):
        self._supporterList = data


