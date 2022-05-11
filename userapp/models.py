from django.db import models
from pygments.lexers import get_all_lexers


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
SKILLS = [('python', 'python'), ('javascript', 'javascript'), ('AWS', 'AWS'), ('Django', 'Django')]
SUPPORT_CHOICES = [('서버 개발비', 'server_pay'), ('AWS 크레딧', 'aws_credit'), ('IDE 지원', 'ide'), ('라이센스 지원', 'license')]


# Create your models here.
class User(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=1000, null=False)
    nickname = models.CharField(max_length=100, null=False)
    img = models.ImageField(null=True)
    bio = models.CharField(max_length=1000)


class Developer(User):
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    skill = models.CharField(choices=SKILLS, default='python', max_length=100)


class Supporter(User):
    can_support = models.CharField(choices=SUPPORT_CHOICES, default='None', max_length=100, null=True)
    will_support = models.CharField(choices=SUPPORT_CHOICES, default='None', max_length=100, null=True)


class Planner(User):
    item = models.CharField( default='None', max_length=100, null=False)