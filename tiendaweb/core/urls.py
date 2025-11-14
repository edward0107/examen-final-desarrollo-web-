from django.urls import path
from . import views


urlpatterns = [
path('', views.inicio, name='inicio'),
path('categorias/', views.categorias, name='categorias'),
path('productos/', views.productos, name='productos'),
path('creditos/', views.creditos, name='creditos'),
]


