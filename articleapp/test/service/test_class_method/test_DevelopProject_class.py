from django.test import TestCase
from articleapp.classes.DevelopProject_class import DevelopProject
from articleapp.classes.Exception_class import ProjectDataIsWrong, ProjectDataIsNotDict


class TestDevelopProject(TestCase):
    """
    make_project
    delete_project
    """

    # 프로젝트 만들기 - 동작 확인
    def test_develop_project_make_project(self):
        # Given
        data = {
            'title': 'test_title',
            'leader': 'test_leader',
            'stack': 'test_stack',
            'due_date': 'test_due_date',
            'desc': 'test_desc',
            'tool': 'test_tool',
        }

        # When
        project = DevelopProject()
        project.make_project(data)

        # Then
        self.assertEqual(project.get_title(), 'test_title')
        self.assertEqual(project.get_title(), 'test_leader')
        self.assertEqual(project.get_title(), 'test_stack')
        self.assertEqual(project.get_title(), 'test_due_date')
        self.assertEqual(project.get_title(), 'test_desc')
        self.assertEqual(project.get_title(), 'test_tool')

    # 프로젝트 만들기 - Key 가 없는 경우
    def test_develop_project_make_project_key_title_is_none(self):
        # Given
        data = {
            'leader': 'test_leader',
            'stack': 'test_stack',
            'due_date': 'test_due_date',
            'desc': 'test_desc',
            'tool': 'test_tool'
        }

        project = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsWrong):
            # When
            project.make_project(data)

    # 프로젝트 만들기 - data가 dict type이 아닐 경우
    def test_develop_project_make_project_data_type_is_not_dict(self):
        # Given
        data = ['test_leader','test_stack','test_due_date','test_desc','test_tool']

        protect = DevelopProject()

        # Then
        with self.assertRaises(ProjectDataIsNotDict):
            # When
            protect.make_project(data)

    def test_develop_project_delete_project(self):
        pass

    def test_develop_project_update_project(self):
        pass

    def test_develop_project_see_now(self):
        pass
