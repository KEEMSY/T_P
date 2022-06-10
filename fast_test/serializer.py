from rest_framework import serializers
from .models import TeamModel, ProjectModel, ArticleModel, Stack, CategoryModel, Comment


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = ['developer', 'leader', 'supporter', 'name']


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ['language', 'img']


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['article', 'team', 'stack', 'title']


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['project', 'title', 'writer', '']


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['developer', 'supporter', 'leader']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['developer', 'supporter', 'leader']
