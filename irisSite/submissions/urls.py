from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('randompost/', views.randompost, name='randompost'),
    path('reportpost/', views.reportpost, name='reportpost'),
]