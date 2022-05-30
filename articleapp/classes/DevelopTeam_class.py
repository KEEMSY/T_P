from .ABC.Team_class import Team
from .Developer_class import Developer
from .Exception_class import TypeIsNotUser, AlreadyMemberExist, MemberDoesNotExist, TypeIsNotDeveloper, \
    TypeIsNotSupporter
from .Supporter_class import Supporter


class DevelopTeam(Team):
    def __init__(self):
        super(DevelopTeam, self).__init__()
        self.set_supporter_list([])

    def make_team(self, data):
        if type(data) is list:
            for user in data:
                if type(user) != Developer:
                    raise TypeIsNotDeveloper
            self.set_team_list(data)
            return True
        else:
            if type(data) != Developer:
                raise TypeIsNotDeveloper
            else:
                self.set_team_list([data])
                return True
        pass

    def append_member(self, data):
        team_list = self.get_team_list()
        for user in team_list:
            if user == data:
                raise AlreadyMemberExist
        return True

    def delete_member(self, data):
        team_list = self.get_team_list()
        if data not in team_list:
            raise MemberDoesNotExist
        else:
            team_list.remove(data)
            self.set_team_list(team_list)
            return True

    def register_leader(self, data):
        if type(data) != Developer:
            raise TypeIsNotDeveloper
        team_list = self.get_team_list()
        if data not in team_list:
            raise MemberDoesNotExist
        self.set_leader(data)
        return True

    def append_supporter(self, data):
        if type(data) is list:
            for supporter in data:
                self.append_supporter(supporter)
            return True

        elif type(data) != Supporter:
            raise TypeIsNotSupporter

        support_list = self.get_supporter_list()
        if data in support_list:
            raise AlreadyMemberExist
        support_list.append(data)
        self.set_supporter_list(support_list)
        return True

    def delete_supporter(self, data):
        if type(data) is list:
            for supporter in data:
                self.delete_member(supporter)
        elif type(data) != Supporter:
            raise TypeIsNotSupporter

        supporter_list = self.get_supporter_list()
        if data in supporter_list:
            supporter_list.remove(data)
        else:
            raise MemberDoesNotExist

    def check(self):
        if len(self.get_team_list()) == 0:
            return False
        elif self.get_leader() is None:
            return False
        else:
            return True
