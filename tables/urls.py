from . import views
from django.urls import path


urlpatterns = [
    path('', views.landing, name='landing'),
    path('upload/', views.home, name='home'),
    path('process', views.process, name='process'),
    path('downloadX/', views.home, name='downloadX'),
    path('downloadC/', views.home, name='downloadC'),
    path('exportJson/', views.home, name='exportJson'),

]




