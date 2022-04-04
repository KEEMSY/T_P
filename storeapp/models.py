from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Store(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='store', null=True)
    #SET_NULL은 회원탈퇴시, 게시글도 지우는 것이아니라, 널값으로 두겠다

    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to='store/', null=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
