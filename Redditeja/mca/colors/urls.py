from django.urls import path
from .import views
urlpatterns=[
    path('red/', views.red, name='red'),
     path('skyblue/', views.skyblue, name='skyblue'),
      path('pink/', views.pink, name='pink'),
      ]
