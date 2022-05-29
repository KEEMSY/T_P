from articleapp.classes.ABC import Project
from userapp.models import SKILLS


class DevelopProject(Project):

    def __init__(self):
        super(DevelopProject, self).__init__()
        self.set_stack([])
        self.set_tool([])

    def make_project(self, data):
        pass

    def update_project(self, target, data):
        pass

    def append_stack(self, data):
        pass

    def delete_stack(self, data):
        pass

    def append_tool(self, data):
        pass

    def delete_tool(self, data):
        pass

    def register_team(self, data):
        pass

    def update_team(self, target, user):
        pass

    def check(self):
        pass

    def see_now(self):
        pass

    def delete_project(self):
        pass
