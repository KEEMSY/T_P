from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from django.test.testcases import TestCase
from articleapp.service.project_db_service import make_article, find_all_article,delete_article, put_article, find_article_one_by_pk
from articleapp.models import DBProjectArticle, DBArticle
from userapp.models import DBUser, DBDeveloper
import random


class TestProjectDBService(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestProjectDBService, self).__init__(*args, **kwargs)
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
    @staticmethod
    def make_right_developer():
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
        print(data)

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
        self.assertFalse(result)

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
        self.assertFalse(result)

    def test_make_article_data_type_is_dict_type(self):
        # Given
        developer = self.make_right_developer()
        data = [1, 2, 3]

        # When
        result = make_article(data)

        # Then
        self.assertFalse(result)

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
        result2 = make_article(data=data2)

        # Then
        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_make_article_article_is_already_exist(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result1 = make_article(data=data)

        # When
        result2 = make_article(data=data)

        # Then
        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_make_article_user_is_exist(self):
        # Given
        data = self.projectArticleRightData

        # When
        result = make_article(data=data)

        # Then
        self.assertFalse(result)

    def test_make_article_category_of_data_is_not_in_category_choice(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        data['category'] = 'aefaefadfa'

        # When
        result = make_article(data=data)

        # Then
        self.assertFalse(result)

    # find_all_article() 관련
    def test_find_all_article(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result = make_article(data=data)

        developer2 = self.make_right_developer()

        while True:
            developer2 = self.make_right_developer()
            if developer2 != developer:
                break

        data2 = self.projectArticleRightData
        data['writer'] = developer2
        data['project_name'] = 'test2_project'
        data['project_desc'] = 'test2_project_desc'
        data['project_due_date'] = '2022-20220'
        data['project_stack'] = 'test2_project_stack'
        data['project_desc'] = 'project_desc'
        result2 = make_article(data2)

        # When
        all_article_list = find_all_article()

        # Then
        self.assertTrue(result)
        self.assertTrue(result2)
        self.assertEqual(len(all_article_list), 2)

        # delete_article
    def test_delete_article_right(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['project_name'] = 'check'
        data['writer'] = developer
        result = make_article(data=data)

        # When
        deleted_article = delete_article(pk=1)

        # Then
        self.assertTrue(result)
        check_article_exist = DBProjectArticle.objects.filter(pk=1).exists()
        self.assertEquals(check_article_exist, False)

    def test_delete_article_what_if_article_does_not_exist(self) :
        # Given
        pk = 12312321
        # When
        with self.assertRaises(ObjectDoesNotExist):
            article = delete_article(pk=pk)

    def test_delete_article_then_user_is_delete(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result = make_article(data=data)

        # When
        article_result = delete_article(pk=1)
        user_result = DBDeveloper.objects.get(pk=1)

        # Then
        self.assertTrue(result)
        self.assertTrue(article_result)
        self.assertEqual(user_result, developer)

    # Put_article Test
    def test_put_article_right_update(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result = make_article(data=data)

        update_data = self.projectArticleRightData

        update_data['project_name'] = 'update_value'
        update_data['writer'] = developer

        # When
        update_result = put_article(pk=1, data=update_data)

        # Then
        self.assertTrue(result)
        self.assertTrue(update_result)
        self.assertEqual('update_value', DBProjectArticle.objects.get(pk=1).project_name)

    def test_put_article_data_type_is_dictionary(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result = make_article(data=data)

        update_data = 'update_value'

        # When Then
        with self.assertRaises(TypeError):
            update_result = put_article(pk=1, data=update_data)

    # find_article_pk
    def test_find_article_by_pk(self):
        # Given
        developer = self.make_right_developer()
        data = self.projectArticleRightData
        data['writer'] = developer
        result = make_article(data=data)
        real_article = DBProjectArticle.objects.get(pk=1)
        # When
        expect_result = find_article_one_by_pk(pk=1)

        # Then
        self.assertEqual(expect_result, real_article)
        self.assertTrue(result)

    def test_find_article_by_pk_has_no_pk(self):
        # Given

        # When
        expect_result = find_article_one_by_pk(pk=9999)

        # Then
        self.assertIsNone(expect_result)

