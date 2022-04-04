from django.urls import path

app_name='bookmarkapp'
urlpatterns= [
    path('subscribes/', SubscriptionView.as_view(), name='subscribes'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]