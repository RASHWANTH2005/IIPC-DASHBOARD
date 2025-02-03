from django.urls import path 
from . import views

urlpatterns = [
    path("" , views.home , name='home'),
    path("create" , views.create , name='create'),
    path("login" , views.loginUser , name='login'),
    path("register" , views.register , name='register'),
    path("logout" , views.logoutUser , name='logout'),
    path("<int:ys>/<int:ye>" , views.year_fil , name='year'),
    path("<str:q>" , views.home , name='search'),
    path("edit/<str:pk>" , views.edit , name='edit'),
    path("delete/<str:pk>" , views.delete , name='delete'),
    path('export/excel/', views.export_to_excel, name='export_to_excel'),

]