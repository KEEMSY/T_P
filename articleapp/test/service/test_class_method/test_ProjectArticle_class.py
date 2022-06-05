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

    # 0 인 상태에서 unlike 할 경우
    def test_project_article_unlike_when_like_is_zero(self):
        # Given
        article = ProjectArticle()

        # When
        article.unlike()
        article.unlike()

        # Then
        self.assertEqual(article.get_like(), 0)

    """
    ------------------------------------------------------------------------------------------------------------------
                                            register_project(data)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 동작 확인
    def test_project_article_register_project(self):
        # Given
        d1 = Developer()
        d2 = Developer()

        article = ProjectArticle()
        data = {
            'title': 'test_project',
            'desc': 'test_desc',
            'due_date': '9999-12-31',
            'developer': [d1, d2],
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
        article.register_project(data)

        # Then
        self.assertEqual(article.get_project().get_title(), project.get_title())
        self.assertEqual(article.get_project().get_desc(), project.get_desc())
        self.assertEqual(article.get_project().get_team().get_leader(), d1)

    # data가 dict 타입이 아닌 경우
    def test_project_article_register_project_when_data_is_not_dict(self):
        # Given
        d1 = Developer()
        d2 = Developer()

        data = ['hello']
        article = ProjectArticle()

        # Then
        with self.assertRaises(TypeError):
            # When
            article.register_project(data)

    # 만들기 실패 한다면 msg : project make fail
    def test_project_article_register_project_when_make_project_fail(self):
        # Given
        d1 = Developer()
        d2 = Developer()

        data = {
            'member': [d1, d2],
            'supporter': [],
            'stack': [],
            'tool': [],
            'skill': [],
            'leader': d1,
        }
        article = ProjectArticle()

        # When
        result = article.register_project(data)

        # Then
        self.assertFalse(result)

    # 만들기 실패 한다면 msg : Team make fail
    def test_project_article_register_project_when_make_team_fail(self):
        # Given
        data = {
            'title': 'test_project',
            'desc': 'test_desc',
            'due_date': '9999-12-31',
            'member': [1, 2],
            'supporter': [],
            'stack': [],
            'tool': [],
            'skill': [],
            'leader': 1,
        }
        article = ProjectArticle()

        # When
        result = article.register_project(data)

        # Then
        self.assertFalse(result)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                    make(data)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 동작 확인
    def test_project_article_make(self):
        # Given
        d1 = Developer()
        article_data = {
            'title': 'test_title',
            'writer': d1,
        }

        # When
        article = ProjectArticle()
        article.make(article_data)

        # Then
        self.assertEqual(article.get_title(), 'test_title')
        self.assertEqual(article.get_writer(), d1)


    """
    ------------------------------------------------------------------------------------------------------------------
                                                update(target, data)
    ------------------------------------------------------------------------------------------------------------------
    """
    def test_project_article_update(self):
        # Given
        d1 = Developer()
        d2 = Developer()

        data = {
            'title': 'test_project',
            'desc': 'test_desc',
            'due_date': '9999-12-31',
            'member': [d1, d2],
            'supporter': [],
            'stack': [],
            'tool': [],
            'skill': [],
            'leader': 1,
        }
        article = ProjectArticle()
        result = article.make(data)

        d3 = Developer()

        # When
        article.update()


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
