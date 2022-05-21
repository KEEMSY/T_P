from articleapp.models import DBProjectArticle
from articleapp.serializer import ProjectArticleSerializer
from typing import Dict


# 기사 만들기
def make_article(data):
    serializer = ProjectArticleSerializer(data=data)
    if serializer.is_valid():
        check = DBProjectArticle.objects.filter(project_name=data['project_name']).exists()
        if check is False:
            serializer.save()
            return True
        else:
            return False
    else:
        print(serializer.errors)
        return False


# 기사 찾기 - 모든 리스트
def find_all_article():
    articles = DBProjectArticle.objects.filter()
    serializer = ProjectArticleSerializer(articles, many=True)
    return serializer.data


# 기사 삭제
def delete_article(pk):
    article = DBProjectArticle.objects.get(pk=pk)
    article.delete()
    return True


# 기사 수정
def put_article(pk, data):
    if type(data) is not dict:
        raise TypeError
    article = DBProjectArticle.objects.get(pk=pk)
    serializer = ProjectArticleSerializer(article, data=data)
    if serializer.is_valid():
        serializer.save()
        return True
    else:
        return False


def find_article_one_by_pk(pk):
    pass