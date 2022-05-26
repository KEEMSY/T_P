from .ABC.Team_class import Team
from .Developer_class import Developer
from .Exception_class import TypeIsNotUser, AlreadyMemberExist, MemberDoesNotExist


class DevelopTeam(Team):
    def __init__(self):
        super(DevelopTeam, self).__init__()

    def make_team(self, data):
        if type(data) is list:
            for user in data:
                if type(user) != Developer:
                    raise TypeIsNotUser
            self.set_team_list(data)
            self.set_supporter([])
            return True
        else:
            if type(data) != Developer:
                raise TypeIsNotUser
            else:
                self.set_team_list([data])
                self.set_supporter([])
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
            raise TypeIsNotUser
        team_list = self.get_team_list()
        if data not in team_list:
            raise MemberDoesNotExist
        self.set_leader(data)
        return True

    def append_supporter(self, data):
        if type(data) != Developer:
            raise TypeIsNotUser

        support_list = self.get_supporter_list()
        support_list.append(data)
        self.set_supporter(support_list)
        return True

    def delete_supporter(self, data):
        if type(data) != Developer:
            raise TypeIsNotUser
        supporter_list = self.get_supporter_list()
        if data in supporter_list:
            supporter_list.remove(data)
        else:
            raise MemberDoesNotExist



