from articleapp.models import DBProjectArticle
from articleapp.serializer import ProjectArticleSerializer


# 기사 만들기
def make_article(data):
    serializer = ProjectArticleSerializer(data=data)
    if serializer.is_valid():
        check = DBProjectArticle.objects.filter(project_name=data['project_name']).exists()
        if check is False:
            serializer.save()
            return "success"
        else:
            return "fail"
    else:
        print(serializer.errors)
        return "fail"


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
def put_article(data):
    article = ProjectArticleSerializer(data=data)
    return article.data
