from django.urls import path
from . import views

app_name = 'python_django_NFSs'
urlpatterns = [
    path('', views.index, name='index'),
    path('storage/<path:dir_name>/', views.files_management, name='manage_files'),
]