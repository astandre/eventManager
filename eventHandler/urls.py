from django.urls import path

from . import views


urlpatterns = [
    path(r'v1/eventos', views.eventos_api, name='eventos_api'),
    path(r'v1/eventos/categoria/<str:categoria>', views.eventos_categoria_api, name='eventos_categoria_api'),
]
