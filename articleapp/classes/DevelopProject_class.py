from articleapp.classes.ABC import Project
from articleapp.classes.Exception_class import ProjectDataIsNotDict, ProjectDataIsWrong, DateIsPasted
from userapp.models import SKILLS
from datetime import datetime
from datetime import date
import re


class DevelopProject(Project):

    def __init__(self):
        super(DevelopProject, self).__init__()
        self.set_stack([])
        self.set_tool([])

    def make_project(self, data):
        # dict 타입 검사
        if type(data) is not dict:
            raise ProjectDataIsNotDict
        # 필수 요소를 갖고 있는지 확인
        if 'title' not in data or 'due_date' not in data or 'desc' not in data:
            raise ProjectDataIsWrong
        # due_date 유효성 검사
        p = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
        if p.search(data['due_date']) is None:
            raise ProjectDataIsWrong

        # 지난 날짜인지 확인
        today = datetime.today().date()
        date_list = data['due_date'].split('-')
        due_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))

        if today > due_date:
            raise DateIsPasted

        self.set_title(data['title'])
        self.set_desc(data['desc'])
        self.set_due_date(data['due_date'])

    def update_project(self, target, data):
        if target == 'title':
            self.set_title(data)
        elif target == 'desc':
            self.set_desc(data)
        elif target == 'due_date':
            # due_date 유효성 검사
            p = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
            if p.search(data) is None:
                raise ProjectDataIsWrong

            # 지난 날짜인지 확인
            today = datetime.today().date()
            date_list = data.split('-')
            due_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))

            if today > due_date:
                raise DateIsPasted
            self.set_due_date(data)
        else:
            return False
        return True

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
