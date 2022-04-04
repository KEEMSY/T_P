from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from userapp import views
from .views import UserCreateView, UserDetailView, UserDeleteView, UserUpdateView

app_name = "userapp"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', UserCreateView.as_view(), name='create'),
    path('update/<int:pk>', UserUpdateView.as_view(),name='update'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete'),

    path('', views.HomeView, name='home'),

]
