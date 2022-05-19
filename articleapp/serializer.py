from rest_framework import serializers
from articleapp.models import DBProjectArticle


class ProjectArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DBProjectArticle
        fields = ['id','title', 'content', 'category', 'contact', 'like', 'create_at', 'update_at', 'writer',
                  'project_name','project_due_date', 'project_stack', 'project_desc', 'project_crew',
                  'project_leader', 'project_support', 'project_status']
