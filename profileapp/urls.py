from django.contrib import admin
from django.urls import path, include

from profileapp.views import ProfileCreateView, ProfileUpdateView
from userapp import views
app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),

]