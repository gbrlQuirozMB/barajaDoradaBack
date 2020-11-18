from django.urls import path, re_path
from rest_auth import urls as urls_rest

from .views import *

app_name = 'api'

urlpatterns = [
    # path('docs/v1.0/', schema_view, ),
    path('docs/v1.0/', SwaggerSchemaView.as_view(), ),
    path('login/', urls_rest.LoginView.as_view()),
    # ----------------------------------------------------------------------------------Carta
    # path('cartas/create/', CartaCreateView.as_view(), ),
    path('cartas/list/', CartaListView.as_view(), ),
    path('cartas/detail/<pk>/', CartaDetailView.as_view(), ),
    path('cartas/update/<pk>/', CartaUpdateView.as_view(), ),
    # path('cartas/delete/<pk>/', CartaDeleteView.as_view(), ),
    path('cartas-disponibles/', CartasDisponiblesListView.as_view(), ),
    # ----------------------------------------------------------------------------------Sorteo
    path('sorteos/create/', SorteoCreateView.as_view(), ),
    path('sorteos/list/', SorteoListView.as_view(), ),
    path('sorteos/detail/<pk>/', SorteoDetailView.as_view(), ),
    path('sorteos/update/<pk>/', SorteoUpdateView.as_view(), ),
    path('sorteos/delete/<pk>/', SorteoDeleteView.as_view(), ),
    # ----------------------------------------------------------------------------------Imagen
    path('imagenes/create/', ImagenCreateView.as_view(), ),
    path('imagenes/list/', ImagenListView.as_view(), ),
    path('imagenes/detail/<pk>/', ImagenDetailView.as_view(), ),
    path('imagenes/update/<pk>/', ImagenUpdateView.as_view(), ),
    path('imagenes/delete/<pk>/', ImagenDeleteView.as_view(), ),
]
