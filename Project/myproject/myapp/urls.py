from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee, name='insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
  # path('master/', views.view_employee,  name = 'master'),
   path('Items/', views.Items,  name = 'Items'),
# other paths as needed
]
