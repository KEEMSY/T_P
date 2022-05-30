from articleapp.classes.ABC import Project
from articleapp.classes.Exception_class import ProjectDataIsNotDict, ProjectDataIsWrong, DateIsPasted, StackDuplicated, \
    StackDoesNotExist, ToolDoesNotExist
from userapp.models import SKILLS
from datetime import datetime
from datetime import date
import re


class DevelopProject(Project):

    def __init__(self):
        super(DevelopProject, self).__init__()
        self.set_stack([])
        self.set_tool([])
        self.skills = []
        for skill in SKILLS:
            self.skills.append(skill[1])

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
        # data 가 있는 skill 인가
        if data not in self.skills:
            raise StackDoesNotExist

        stack = self.get_stack()
        if data not in stack:
            stack.append(data)
        else:
            # 중복된 skill 일 경우
            raise StackDuplicated

    def delete_stack(self, data):
        stack = self.get_stack()
        if data not in stack:
            raise StackDoesNotExist

        stack.remove(data)
        self.set_stack(stack)

    def append_tool(self, data):
        tools = self.get_tool()
        if data not in tools:
            tools.append(data)
        else:
            raise ToolDoesNotExist

    def delete_tool(self, data):
        tools = self.get_tool()
        if data not in tools:
            raise ToolDoesNotExist
        tools.remove(data)

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
