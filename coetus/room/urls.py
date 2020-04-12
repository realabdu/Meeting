from . import views
from django.urls import path
urlpatterns = [

    path('demo/', views.demo, name='demo'),
    path('demo/<id>', views.demo, name='demoPDF'),
    path('', views.landing, name='landing'),

]
