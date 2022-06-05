from . import DevelopProject, DevelopTeam, Developer
from .ABC import Article


# ProjectArticle
from .Exception_class import TitleDoesNotExist, WriterDoesNotExist, TypeIsNotDeveloper


class ProjectArticle(Article):
    def __init__(self):
        super(ProjectArticle, self).__init__()
        self._like = 0

    def like(self):
        self._like += 1

    def unlike(self):
        self._like -= 1
        if self._like < 0:
            self._like = 1

    def register_project(self, data):
        if type(data) is not dict:
            raise TypeError
        try:
            project = DevelopProject()
            project.make_project(data)

            team = DevelopTeam()
            team.make_team(data['developer'])
            team.register_leader(data['leader'])
            team.append_supporter(data['supporter'])
            if team.check is False:
                return False

            project.register_team(team)
            self.set_project(project)

        except Exception as e:
            print(e)
            return False

    def make(self, data):
        if type(data) is not dict:
            raise TypeError
        if 'title' not in data:
            raise TitleDoesNotExist
        if 'writer' not in data:
            raise WriterDoesNotExist

        self.set_title(data['title'])
        self.set_writer(data['writer'])

    def update(self, target, data):
        if target == 'title':
            if type(data) is not str:
                raise TypeError
            self.set_title(data)
        elif target == 'writer':
            if type(data) is not Developer:
                raise TypeIsNotDeveloper
            self.set_writer(data)

    def delete(self):
        self.set_project(None)
        self.set_writer(None)
        self.set_title(None)
        self.set_like(None)
        self.set_pk(None)
        self.set_comment(None)

    def report(self):
        pass

    def contact(self):
        pass




