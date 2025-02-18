from django.urls import path
from django.contrib import admin
#now import the views.py file into this code
from . import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.view_student, name='view_student'),
    path('add_student/', views.add_student, name='add_student'),
]
