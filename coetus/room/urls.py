from . import views
from django.urls import path
urlpatterns = [

    path('demo/', views.demo, name='demo'),
    path('', views.landing, name='landing'),

]
