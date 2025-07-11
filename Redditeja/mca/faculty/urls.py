from django.urls import path
from .import views
urlpatterns=[
    path('Reddy/' ,views.Reddy, name='Reddy'),
    path('Teja/', views.Teja, name='Teja'),
    path('First' ,views.First, name='First'),
    path('home/' ,views.home, name='home'),
    ]
