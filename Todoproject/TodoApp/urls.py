from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Home,name='Home'),
    path('details/<int:id>',views.Details,name='details'),
  
]