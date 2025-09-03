from django.urls import path
from . import views


urlpatterns = [
  path('list/', views.churches, name='churches'),
  path('save/', views.create_church, name='create_church'),
  path('edit/<int:id>', views.edit_church, name='edit_church'),
]