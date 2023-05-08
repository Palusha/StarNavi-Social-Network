from django.urls import path

from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.LikeCountView.as_view(), name='likes-count'),
]