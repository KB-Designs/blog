from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#app_name='blog'


urlpatterns=[
    path('',views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view,
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    

]