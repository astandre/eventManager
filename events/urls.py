from django.conf.urls import url

from . import views

# app_name = 'eventos'
urlpatterns = [
    url(r'^eventos/$', views.EventosList.as_view(), name=views.EventosList.name),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.EventosDetail.as_view(), name=views.EventosDetail.name),
    url(r'^locales/$', views.LocalesList.as_view(), name=views.LocalesList.name),
    url(r'^local/(?P<pk>[0-9]+)/$', views.LocalesDetail.as_view(), name=views.LocalesDetail.name),
    url(r'^evento/categoria/(?P<cod_categoria>[A-Z]{1})/$', views.EventosCategoriaFilter.as_view()),
]
