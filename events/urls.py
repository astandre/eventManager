from django.conf.urls import url

from . import views
app_name = 'eventos'
urlpatterns = [
    url(r'^$', views.EventosView.as_view(), name='eventos'),

]