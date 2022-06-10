from django.urls import path
from fast_test.api.team_api import TeamView, TeamDetailView
urlpatterns = [
    path('team/', TeamView.as_view(), name='Team_view'),
    path('team/<int:pk>', TeamDetailView.as_view(), name='Team_detail_view'),

]