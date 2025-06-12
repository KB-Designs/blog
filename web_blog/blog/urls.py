from django.urls import path
from . import views

app_name='blog'


urlpatterns=[
    path('', views.home, name='post_list'),
    path('about/', views.about, name='about'),
]