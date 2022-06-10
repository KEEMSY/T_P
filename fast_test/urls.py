from django.urls import path
from fast_test.api.team_api import TeamView
urlpatterns = [
    path('team/', TeamView.as_view(), name='Team_view'),
]