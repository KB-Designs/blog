from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='blog'


urlpatterns=[
    path('', views.home, name='post_list'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name='about'),
]