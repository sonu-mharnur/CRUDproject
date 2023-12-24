
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('deleteuser/<int:id>', views.deleteme, name='delete'),
    path('edituser/<int:id>', views.editme, name='edit'),
    path('searchdata/', views.searchdata, name='search'),
    
]