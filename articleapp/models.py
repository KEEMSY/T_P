from django.db import models
from userapp.models import User, Developer, Supporter, Planner


CATEGORY_CHOICE = [('project', 'project'), ('question', 'question')]


class Article(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    category = models.CharField(choices=CATEGORY_CHOICE, default='project', max_length=100)
    contact = models.CharField(max_length=100, default='')
    like = models.IntegerField(default=0)
    create_at = models.TimeField(auto_now=True)
    update_at = models.TimeField(auto_now=True)


class ProjectArticle(Article):
    writer = models.ForeignKey(Developer, related_name='user_writer', on_delete=models.CASCADE)
    project_name = models.CharField(default='', max_length=100, null=False)
    project_due_date = models.CharField(default='', max_length=100, null=False)
    project_stack = models.CharField(default='', max_length=100, null=False)
    project_desc = models.CharField(default='', max_length=100, null=False)
    project_crew = models.ForeignKey(User, related_name='user_crew', on_delete=models.SET_NULL, null=True)
    project_leader = models.ForeignKey(User, related_name='user_leader', on_delete=models.CASCADE)
    project_support = models.ManyToManyField(User, related_name='user_support')
    project_satus = models.BooleanField(default=True)