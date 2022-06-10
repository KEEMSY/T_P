from django.db import models
from userapp.models import DBDeveloper, DBSupporter
from articleapp.models import DBArticle


# Create your models here.
class TeamModel(models.Model):
    name = models.CharField(max_length=100, default=f'NewTeam')
    developer = models.ManyToManyField(DBDeveloper, related_name='developer', null=True)
    supporter = models.ManyToManyField(DBSupporter, related_name='supporter', null=True)
    leader = models.ForeignKey(DBDeveloper, on_delete=models.CASCADE, related_name='leader', null=True)
    create_at = models.TimeField(auto_created=True)
    update_at = models.TimeField(auto_now=True)


class Stack(models.Model):
    language = models.CharField(max_length=100)
    img = models.ImageField()


class ProjectModel(models.Model):
    article = models.ManyToManyField(DBArticle)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
    stack = models.ManyToManyField(Stack)
    title = models.CharField(max_length=100)
    create_at = models.TimeField(auto_created=True)
    update_at = models.TimeField(auto_now=True)


class ArticleModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(DBDeveloper, on_delete=models.CASCADE)
    create_at = models.TimeField(auto_created=True)
    update_at = models.TimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    writer = models.ForeignKey(DBDeveloper, on_delete=models.CASCADE)
    context = models.CharField(max_length=100)
    create_at = models.TimeField(auto_created=True)
    update_at = models.TimeField(auto_now=True)


class CategoryModel(models.Model):
    article = models.ManyToManyField(ArticleModel)
    subject = models.CharField(max_length=100)

