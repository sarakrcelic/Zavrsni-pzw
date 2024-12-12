from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]