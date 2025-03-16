from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<str:topic_name>/', views.topic_view, name='topic_view'),
]
