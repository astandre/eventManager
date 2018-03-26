from django.conf.urls import url

from . import views

# app_name = 'eventos'
urlpatterns = [
    url(r'^events/$', views.EventosList.as_view(), name=views.EventosList.name),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventosDetail.as_view(), name=views.EventosDetail.name),
    url(r'^locales/$', views.LocalesList.as_view(), name=views.LocalesList.name),
    url(r'^locales/(?P<pk>[0-9]+)/$', views.LocalesDetail.as_view(), name=views.LocalesDetail.name),
    url(r'^categoria/$', views.CategoriasList.as_view(), name=views.CategoriasList.name),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoriaDetail.as_view(), name=views.CategoriaDetail.name),
]
