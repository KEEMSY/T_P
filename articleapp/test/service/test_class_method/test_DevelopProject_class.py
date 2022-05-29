from django.test import TestCase

from articleapp.classes import Developer, DevelopTeam
from articleapp.classes.DevelopProject_class import DevelopProject
from articleapp.classes.Exception_class import ProjectDataIsWrong, ProjectDataIsNotDict, TypeIsNotDeveloper


class TestDevelopProject(TestCase):
    """
        DevelopProject TestCase
        * make_project(data: Dict)
        * update_project(target, data)

        * append_stack(data)
        * delete_stack(data)

        * append_tool(data)
        * delete_tool(data)

        * register_team(data)
        * update_team(target, data)

        * check()
        * see_now()
    """
    """
    ------------------------------------------------------------------------------------------------------------------
                                                make_project(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 동작 확인
    def test_develop_project_make_project(self):
        # Given
        data = {
            'title': 'test_title',
            'due_date': 'test_due_date',
            'desc': 'test_desc',
        }

        # When
        project = DevelopProject()
        project.make_project(data)

        # Then
        self.assertEqual(project.get_title(), 'test_title')
        self.assertEqual(project.get_due_date(), 'test_due_date')
        self.assertEqual(project.get_desc(), 'test_desc')

    # title 이 없는 경우
    def test_develop_project_make_project_when_data_has_not_title(self):
        # Given
        data = {
            'due_date': 'test_due_date',
            'desc': 'test_desc',
        }

        project = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsWrong):
            # When
            project.make_project(data)

    # due_date가 없는 경우
    def test_develop_project_make_project_when_data_type_has_not_due_date(self):
        # Given
        data = {
            'title': 'test_title',
            'desc': 'test_desc',
        }

        project = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsWrong):
            # When
            project.make_project(data)

    # desc 가 없는 경우
    def test_develop_project_make_project_when_data_type_has_not_desc(self):
        # Given
        data = {
            'title': 'test_title',
            'due_date': 'test_due_date',
        }

        project = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsWrong):
            # When
            project.make_project(data)

    # 프로젝트 만들기 - data가 dict type이 아닐 경우
    def test_develop_project_make_project_data_leader_is_not_dict(self):
        # Given
        data = ['test_leader', 'test_due_date', 'test_desc']

        protect = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsNotDict):
            # When
            protect.make_project(data)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    update_title(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 프로젝트 업데이트 - 프로젝트 이름 변경
    def test_develop_project_update_title(self):
        # Given
        data = {
            'leader': 'test_leader',
            'stack': 'test_stack',
            'due_date': 'test_due_date',
            'desc': 'test_desc',
            'tool': 'test_tool'
        }

        project = DevelopProject()
        project.make_project(data)

        # When
        project.update_project(target='title', data='update_title')

        # Then
        self.assertEqual(project.get_title(), 'update_title')

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    append_stack(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 프로젝트 스택 추가 - 동작 테스트
    def test_develop_project_append_stack(self):
        # Given
        d1 = Developer()

        data = {
            'title': 'test_title',
            'due_date': 'test_due_date',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)

        # When
        project.append_stack(data='stack1')

        # Then
        self.assertEqual(project.get_stack(), ['stack1'])

    """
    ------------------------------------------------------------------------------------------------------------------
                                                   delete_stack(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 프로젝트 스택 삭제 - 동작 확인
    def test_develop_project_delete_stack(self):
        pass

    """
    ------------------------------------------------------------------------------------------------------------------
                                                update_team(target, data)
    ------------------------------------------------------------------------------------------------------------------
    """


    # 프로젝트 업데이트 팀 - 프로젝트 리더 변경
    def test_develop_project_update_leader(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)

        data = {
            'title': 'test_title',
            'due_date': 'test_due_date',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)

        # When
        project.update_team('leader', d2)

        # Then
        self.assertEqual(project.get_team().get_leader(), d2)


    def test_develop_project_see_now(self):
        pass

    # 프로젝트 삭제 -
    def test_develop_project_delete_project(self):
        # Given
        data = {
            'title': 'test_title',
            'due_date': 'test_due_date',
            'desc': 'test_desc'
        }

        team = DevelopTeam()
        d1 = Developer()
        d2 = Developer()
        team.make_team(d1)
        team.make_team(d2)
        team.set_leader(d1)

        project = DevelopProject()
        project.make_project(data)

        project.append_stack('python')
        project.append_tool('notion')

        project.register_team(team)

        # When
        project.delete_project()

        # Then
