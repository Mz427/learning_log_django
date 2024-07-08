from django.urls import path
from . import views

app_name = 'python_django_NFSs'
urlpatterns = [
    path('', views.index, name='index'),
]