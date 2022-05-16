from django.test.testcases import TestCase
from articleapp.service.project_db_service import make_article
from articleapp.models import DBProjectArticle
from userapp.models import DBUser, DBDeveloper
import random


class TestProjectDBService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestProjectDBService, self).__init__( *args, **kwargs)
        self.projectArticleRightData = {
            'title': 'test_title',
            'content': 'test_content',
            'category': 'project',
            'contact': 'test_contact',
            'writer': None,
            'project_name': 'test_project_name',
            'project_due_date': 'test_project_due_date',
            'project_stack': 'test_project_stack',
            'project_desc': 'test_project_desc',
        }

    # Given
    # When
    # Then
    def make_right_developer(self):
        email_list = ["zhqmfkv@naver.com", "aaa@naver.com", "ba@naver.com" ,"adfasdfdasf@naver.com"]
        password_list = ["423412", "23423432", "234234234"]
        nickname_list = ["423412", "23423432", "234234234"]
        bio_list = ["adfadsfadsf", "2342343asdfadsfadsf2", "234asdfasdf34234"]
        email = random.choice(email_list)
        password = random.choice(password_list)
        nickname = random.choice(nickname_list)
        bio = random.choice(bio_list)
        developer = DBDeveloper.objects.create(email=email, password=password, nickname=nickname, bio=bio)
        return developer

    def test_check_make_article(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer

        # When
        result = make_article(data=data)

        # then
        check = DBProjectArticle.objects.get(pk=1)
        self.assertIsNotNone(check)

    def test_make_article_data_is_checked(self):
        # Given
        developer = self.make_right_developer()
        wrong_data = {
            'wrong': 'data'
        }
        # When
        result = make_article(data=wrong_data)

        # Then
        self.assertEqual(result, "fail")

    def test_make_article_data_is_necessary_data(self):
        # Given
        developer = self.make_right_developer()
        wrong_data = {
            'project_name': 'test_project_name',
            'project_due_date': 'test_project_due_date',
            'project_stack': 'test_project_stack',
            'project_desc': 'test_project_desc',
        }

        # When
        result = make_article(data=wrong_data)

        # Then
        self.assertEqual(result, "fail")

    def test_make_article_data_type_is_dict_type(self):
        # Given
        developer = self.make_right_developer()
        data = [1, 2, 3]

        # When
        result = make_article(data)

        # Then
        self.assertEqual(result, "fail")

    def test_make_article_project_already_exist(self):
        # Given
        developer1 = self.make_right_developer()
        data1 = self.projectArticleRightData
        data1['writer'] = developer1
        result1 = make_article(data=data1)

        # When
        developer2 = self.make_right_developer()
        data2 = self.projectArticleRightData
        data2['writer'] = developer2
        reuslt2 = make_article(data=data2)

        # Then
        self.assertEqual(result1, "success")
        self.assertEqual(reuslt2, "fail")

    def test_make_article_article_is_already_exist(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result1 = make_article(data=data)

        # When
        result2 = make_article(data=data)

        # Then
        self.assertEqual(result1, "success")
        self.assertEqual(result2, "fail")

    def test_make_article_user_is_exist(self):
        # Given
        data = self.projectArticleRightData

        # When
        result = make_article(data=data)

        # Then
        self.assertEqual(result, "fail")

    def test_make_article_category_of_data_is_not_in_category_choice(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        data['category'] = 'aefaefadfa'

        # When
        result = make_article(data=data)

        # Then
        self.assertEqual(result, 'fail')

