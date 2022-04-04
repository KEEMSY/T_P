from django.urls import path
from django.views.generic import TemplateView

app_nmae='storeapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='storeapp:list.html'), name='list')
]