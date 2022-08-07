from django.urls import path
from . import views
urlpatterns = [
    path('page2.html', views.page2,name = 'page2'),
    path('home/', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path(r'^foo/',views.download),


    
]   