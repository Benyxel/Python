from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register') ,
    path('read_notes/', views.read_notes, name = 'allnotes'),
    path('persons/', views.persons, name= 'persons'),
    path('details/<int:id>', views.read_note_single, name = 'details_read' )
]