from django.conf.urls import url

from . import views

# app_name = 'eventos'
urlpatterns = [
    url(r'^eventos/$', views.EventosList.as_view(), name=views.EventosList.name),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.EventosDetail.as_view(), name=views.EventosDetail.name),
    url(r'^locales/$', views.LocalesList.as_view(), name=views.LocalesList.name),
    url(r'^local/(?P<pk>[0-9]+)/$', views.LocalesDetail.as_view(), name=views.LocalesDetail.name),
    url(r'^categorias/$', views.CategoriasList.as_view(), name=views.CategoriasList.name),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoriaDetail.as_view(), name=views.CategoriaDetail.name),
    url(r'^evento/categoria/(?P<cod_categoria>[0-9]+)/$', views.EventosCategoriaFilter.as_view()),
]
