from . import DevelopProject, DevelopTeam
from .ABC import Article


# ProjectArticle
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

    def make(self, data):
        if type(data) is not dict:
            raise TypeError
        try:
            project = DevelopProject()
            project.make_project(data)
            team = DevelopTeam()
            team.make_team(data['developer'])
            team.set_leader(data['leader'])
            for supporter in data['supporter']:
                team.append_supporter(supporter)
            project.register_team(team)
            self.set_project(project)
            return True
        except Exception as e:
            return False

    def update(self, target, data):
        pass

    def delete(self):
        pass

    def report(self):
        pass

    def contact(self):
        pass




