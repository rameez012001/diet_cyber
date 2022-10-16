from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deleteall/', views.deleteall, name='deleteall'),
    path('delete/<int:id>', views.delete, name='delete'),
]
