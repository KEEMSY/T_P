from django.test import TestCase

from articleapp.classes import ProjectArticle, DevelopProject, DevelopTeam, Developer


class TestProjectArticle(TestCase):
    """
    * like():
    * unlike():
    * make():
    * update(target, data):
    * delete():
    * report():
    * contact():

    """

    """
    ------------------------------------------------------------------------------------------------------------------
                                                like(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 동작 테스트
    def test_project_article_like(self):
        # Given
        article = ProjectArticle()

        # When
        article.like()

        # Then
        self.assertEqual(article.get_like(), 1)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                unlike(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
    def test_project_article_unlike(self):
        # Given
        article = ProjectArticle()
        article.like()

        # When
        article.unlike()

        # Then
        self.assertEqual(article.get_like(), 0)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    make(data)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 동작 확인
    def test_project_article_make(self):
        # Given
        d1 = Developer()
        d2 = Developer()

        article = ProjectArticle()
        data = {
            'title': 'test_project',
            'desc': 'test_desc',
            'due_date': '9999-12-31',
            'member': [d1, d2],
            'supporter': [],
            'stack': [],
            'tool': [],
            'skill': [],
            'leader': d1,
        }

        project = DevelopProject()
        project.make_project(data)

        team = DevelopTeam()

        # When
        article.make(data)

        # Then
        self.assertEqual(article.get_project().get_title(), project.get_title())
        self.assertEqual(article.get_project().get_desc(), project.get_desc())
        self.assertEqual(article.get_project().get_team().get_leader(), d1)

    # 동작 확인


    """
    ------------------------------------------------------------------------------------------------------------------
                                                update(target, data)
    ------------------------------------------------------------------------------------------------------------------
    """
    def test_project_article_update(self):
        # Given
        article = ProjectArticle()


    """
    ------------------------------------------------------------------------------------------------------------------
                                                delete(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
    """
    ------------------------------------------------------------------------------------------------------------------
                                                report(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
