from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
     path('register/', views.logout_user, name='register') 
]