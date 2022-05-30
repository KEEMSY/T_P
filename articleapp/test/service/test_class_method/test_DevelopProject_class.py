from django.test import TestCase

from articleapp.classes import Developer, DevelopTeam
from articleapp.classes.DevelopProject_class import DevelopProject
from articleapp.classes.Exception_class import ProjectDataIsWrong, \
    ProjectDataIsNotDict, TypeIsNotDeveloper, StackDuplicated, StackDoesNotExist, ToolDoesNotExist, \
    TypeIsNotDevelopTeam, TeamIsNotOkay, DateIsPasted


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
            'due_date': '9999-12-31',
            'desc': 'test_desc',
        }

        # When
        project = DevelopProject()
        project.make_project(data)

        # Then
        self.assertEqual(project.get_title(), 'test_title')
        self.assertEqual(project.get_due_date(), '9999-12-31')
        self.assertEqual(project.get_desc(), 'test_desc')

    # title 이 없는 경우
    def test_develop_project_make_project_when_data_has_not_title(self):
        # Given
        data = {
            'due_date': '9999-12-31',
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

    # due_date 가 오늘 보다 이전일 경우
    def test_develop_project_make_project_when_due_date_is_past(self):
        # Given
        data = {
            'title': 'test_title',
            'desc': 'test_desc',
            'due_date': '9999-12-31'
        }
        project = DevelopProject()

        # Then
        with self.assertRaises(DateIsPasted):
            # When
            project.make_project(data)

    # desc 가 없는 경우
    def test_develop_project_make_project_when_data_type_has_not_desc(self):
        # Given
        data = {
            'title': 'test_title',
            'due_date': '9999-12-31',
        }

        project = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsWrong):
            # When
            project.make_project(data)

    # data가 dict type이 아닐 경우
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

    # 프로젝트 이름 변경
    def test_develop_project_update_title(self):
        # Given
        data = {
            'due_date': '9999-12-31',
            'desc': 'test_desc',
            'title': 'test_title'
        }

        project = DevelopProject()
        project.make_project(data)

        # When
        project.update_project(target='title', data='update_title')

        # Then
        self.assertEqual(project.get_title(), 'update_title')

    # 프로젝트 마감 날짜 변경
    def test_develop_project_update_due_date(self):
        # Given
        data = {
            'due_date': '9999-12-31',
            'desc': 'test_desc',
            'title': 'test_title'
        }

        project = DevelopProject()
        project.make_project(data)

        # When
        project.update_project(target='due_date', data='9999-12-31')

        # Then
        self.assertEqual(project.get_due_date(), '9999-12-31')

    # 프로젝트 설명 변경
    def test_develop_project_update_desc(self):
        # Given
        data = {
            'due_date': '9999-12-31',
            'desc': 'test_desc',
            'title': 'test_title'
        }

        project = DevelopProject()
        project.make_project(data)

        # When
        project.update_project(target='desc', data='이번 프로젝트는 이겁니다!')

        # Then
        self.assertEqual(project.get_desc(), '이번 프로젝트는 이겁니다!')

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    append_stack(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 테스트
    def test_develop_project_append_stack(self):
        # Given
        project = DevelopProject()

        # When
        project.append_stack(data='python')

        # Then
        self.assertEqual(project.get_stack(), ['python'])

    # 동일한 스택이 들어 가는 경우
    def test_develop_project_append_stack_when_same_stack_appended(self):
        # Given
        project = DevelopProject()
        project.append_stack(data='python')

        # Then
        with self.assertRaises(StackDuplicated):
            # When
            project.append_stack(data='python')

    # 스택이 정해진 리스트에 없을 때
    def test_develop_project_append_stack_when_stack(self):
        # Given
        project = DevelopProject()

        # Then
        with self.assertRaises(StackDoesNotExist):
            # When
            project.append_stack(data='stack1')

    """
    ------------------------------------------------------------------------------------------------------------------
                                                   delete_stack(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 확인
    def test_develop_project_delete_stack(self):
        # Given
        project = DevelopProject()
        project.append_stack('python')

        # When
        project.delete_stack('python')

        # Then
        self.assertEqual(project.get_stack(), [])

    # 없는 스택을 삭제할 경우
    def test_develop_project_delete_stack_when_stack_does_not_exist(self):
        # Given
        project = DevelopProject()

        # Then
        with self.assertRaises(StackDoesNotExist):
            # When
            project.delete_stack('python')

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    append_tool(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 확인
    def test_develop_project_append_tool(self):
        # Given
        project = DevelopProject()

        # When
        project.append_tool('notion')

        # Then
        self.assertEqual(project.get_tool(), ['notion'])

    # 이미 있는 tool를 추가하는 경우
    def test_develop_project_append_when_tool_is_already_exist(self):
        # Given
        project = DevelopProject()
        project.append_tool('notion')

        # Then
        with self.assertRaises(ToolDoesNotExist):
            # When
            project.append_tool('notion')

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    delete_tool(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 확인
    def test_develop_project_delete_tool(self):
        # Given
        project = DevelopProject()
        project.append_tool('notion')

        # When
        project.delete_tool('notion')

        # Then
        self.assertEqual(project.get_tool(), [])

    # 없는 tool를 삭제할 경우
    def test_develop_project_delete_tool_when_tool_does_not_exist(self):
        # Given
        project = DevelopProject()

        # Then
        with self.assertRaises(ToolDoesNotExist):
            # When
            project.delete_tool('notion')

    """
    ------------------------------------------------------------------------------------------------------------------
                                                register_team(data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 확인
    def test_develop_project_register_team(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])

        project = DevelopProject()

        # When
        project.register_team(team)

        # Then
        self.assertEqual(project.get_team(), team)

    # data 가 DevelopTeam 이 아닌 경우
    def test_develop_project_register_team_when_Type_is_not_DevelopTeam(self):
        # Given
        d1 = Developer()
        project = DevelopProject()

        # Then
        with self.assertRaises(TypeIsNotDevelopTeam):
            # When
            project.register_team(d1)

    # Team 이 갖춰 지지 않은 경우
    def test_develop_project_register_team_when_team_does_not_okay(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        project = DevelopProject()

        # Then
        with self.assertRaises(TeamIsNotOkay):
            # When
            project.register_team(team)


    """
    ------------------------------------------------------------------------------------------------------------------
                                                update_team(target, data)
    ------------------------------------------------------------------------------------------------------------------
    """

    # 프로 젝트 리더 변경
    def test_develop_project_update_leader(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)

        data = {
            'title': 'test_title',
            'due_date': '9999-12-31',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)

        # When
        project.update_team('leader', d2)

        # Then
        self.assertEqual(project.get_team().get_leader(), d2)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    check()
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 확인
    def test_develop_project_check(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)

        data = {
            'title': 'test_title',
            'due_date': '9999-12-31',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)

        # When
        result = project.check()

        # Then
        self.assertTrue(result)

    # 팀이 없을 경우
    def test_develop_project_check_when_team_is_not_building(self):
        # Given
        data = {
            'title': 'test_title',
            'due_date': '9999-12-31',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)

        # When
        result = project.check()

        # Then
        self.assertFalse(result)

    # 제목이 없을 경우
    def test_develop_project_check_when_title_is_None(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)

        data = {
            'due_date': '9999-12-31',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)

        # When
        result = project.check()

        # Then
        self.assertFalse(result)

    # due_date 가 없을 경우
    def test_develop_project_check_when_due_date_is_None(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)

        data = {
            'title': 'test_title',
            'desc': 'test_desc',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)

        # When
        result = project.check()

        # Then
        self.assertFalse(result)

    # desc 가 없을 경우
    def test_develop_project_check_when_desc_is_None(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)

        data = {
            'title': 'test_title',
            'due_date':'9999-12-31',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)

        # When
        result = project.check()

        # Then
        self.assertFalse(result)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    see_now()
    ------------------------------------------------------------------------------------------------------------------
    """

    # 동작 확인
    def test_develop_project_see_now(self):
        # Given
        d1 = Developer()
        d2 = Developer()
        d1.set_nickname('devel1')
        d1.set_nickname('devel2')
        team = DevelopTeam()
        team.make_team([d1, d2])
        team.set_leader(d1)
        team.register_leader(d1)

        data = {
            'desc' : 'test_desc',
            'title': 'test_title',
            'due_date': '9999-2-20',
        }

        project = DevelopProject()
        project.make_project(data)
        project.register_team(team)


        # When
        result = project.see_now()

        # Then
        expect = {
            'desc': 'test_desc',
            'title': 'test_title',
            'due_date': '9999-2-20',
            'team': ['devel1', 'devel1'],
            'leader': ['devel1'],
            'tool': [],
            'stack': [],
        }
        self.assertDictEqual(expect, result)

