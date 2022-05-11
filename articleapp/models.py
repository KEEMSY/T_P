from django.db import models
from userapp.models import User, Developer, Supporter, Planner


CATEGORY_CHOICE = [('project', 'project'), ('question', 'question')]


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    category = models.CharField(choices=CATEGORY_CHOICE, default='project', max_length=100)
    contact = models.CharField(max_length=100, default='')
    like = models.IntegerField(default=0)
    create_at = models.TimeField(auto_now=True)
    update_at = models.TimeField(auto_now=True)


class ProjectArticle(Article):
    writer = models.ForeignKey(Developer, related_name='writer', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=100)
    project_skill = models.CharField(max_length=100)


class DevlopTeam(models.Model):
    project = models.ForeignKey(ProjectArticle, related_name='project', on_delete=models.CASCADE)
    crew = models.ForeignKey(Developer, related_name='crew', on_delete=models.CASCADE)
    leader = models.ForeignKey(Developer, related_name='leader', on_delete=models.CASCADE)
