from django.test import TestCase

from articleapp.classes import ProjectArticle, DevelopProject, DevelopTeam, Developer
from articleapp.classes.Exception_class import TitleDoesNotExist, WriterDoesNotExist, TypeIsNotDeveloper


class TestProjectArticle(TestCase):
    """
    * like():
    * unlike():
    * make(data):
    * register_project(data)
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

    # dict 타입이 아닐 경우 -> TypeError
    def test_project_article_make_when_data_is_not_dict(self):
        # Given
        article_data = ['test_title', 'writer']

        # Then
        with self.assertRaises(TypeError):
            # When
            article = ProjectArticle()
            article.make(article_data)

    # title 이 없는 경우 -> False
    def test_project_article_make_when_title_is_none_or_empty(self):
        # Given
        d1 = Developer()
        article_data = {
            'title' : '',
            'writer': d1,
        }

        # When
        article = ProjectArticle()
        result = article.make(article_data)

        # Then
        self.assertFalse(result)

    # writer 가 없는 경우 -> False
    def test_project_article_make_when_writer_is_None(self):
        # Given
        article_data = {
            'title': 'test_title',
            'writer': None
        }

        # When
        article = ProjectArticle()
        result = article.make(article_data)

        # Then
        self.assertFalse(result)

    # title key 값이 없는 경우 -> False
    def test_project_article_make_when_title_key_is_None(self):
        # Given
        d1 = Developer()
        article_data = {
            'example1' : 'ex1',
            'writer' : d1
        }

        # Then
        with self.assertRaises(TitleDoesNotExist):
            # When
            article = ProjectArticle()
            article.make(article_data)

    # writer key 값이 없는 경우 -> False
    def test_project_article_make_when_writer_key_is_None(self):
        # Given
        article_data = {
            'title': 'ex1',
            'example': 'ex2'
        }

        # Then
        with self.assertRaises(WriterDoesNotExist):
            # When
            article = ProjectArticle()
            article.make(article_data)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                update(target, data)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 작성자 변경
    def test_project_article_update_writer_update(self):
        # Given
        d1 = Developer()
        d2 = Developer()

        article_data = {
            'title': 'test_project',
            'writer': d1
        }
        article = ProjectArticle()
        article.make(article_data)

        # When
        article.update('writer', d2)

        # Then
        self.assertEqual(article.get_writer(), d2)

    # 변경할 작성자가 Developer 타입이 아닐경우
    def test_project_article_update_when_writer_is_not_developer_type(self):
        # Given
        d1 = Developer()
        article_data = {
            'title': 'test_project',
            'writer': d1
        }
        article = ProjectArticle()
        article.make(article_data)


        # Then
        with self.assertRaises(TypeIsNotDeveloper):
            # When
            article.update('writer', 'd2')

    # 게시글 이름 변경
    def test_project_article_update_title_update(self):
        # Given
        d1 = Developer()

        article_data = {
            'title': 'test_project',
            'writer': d1
        }
        article = ProjectArticle()
        article.make(article_data)

        # When
        article.update('title', 'update_title')

        # Then
        self.assertEqual(article.get_title(), 'update_title')

    # 게시글이 String이 type 아닐 경우 -> TypeError
    def test_project_article_update_when_updated_title_is_not_sting(self):
        # Given
        d1 = Developer()

        article_data = {
            'title': 'test_project',
            'writer': d1
        }
        article = ProjectArticle()
        article.make(article_data)

        # Then
        with self.assertRaises(TypeError):
            # When
            article.update('title', 1)

    """
    ------------------------------------------------------------------------------------------------------------------
                                                delete(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
    # 동작확인
    def test_project_article_delete(self):
        # Given
        d1 = Developer()

        data = {
            'title': 'test_title',
            'writer': d1
        }
        article = ProjectArticle()
        # When
        article.delete()

        # Then
        self.assertIsNone(article.get_project())
        self.assertIsNone(article.get_title())
        self.assertIsNone(article.get_writer())
        self.assertIsNone(article.get_pk())
        self.assertIsNone(article.get_comment())
        self.assertIsNone(article.get_like())

    """
    ------------------------------------------------------------------------------------------------------------------
                                                report(data: Dict)
    ------------------------------------------------------------------------------------------------------------------
    """
