from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register') ,
    path('read_notes/', views.read_notes, name=' read_notes '),
    path('note_page/', views.notepage, name= ' note_page')
]