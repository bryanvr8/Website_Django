from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('cliente/', views.cliente, name = 'cliente'),
    path('create/', views.create, name= 'create'),
    path('read/', views.read, name= 'read'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]