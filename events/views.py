from django.shortcuts import render

# Create your views here.
#  from django.contrib.auth.models import User, Group UserSerializer, GroupSerializer,
from rest_framework import viewsets
from events.serializers import  EventSerializer, LocalSerializer, CategoriaSerializer
from events.models import Evento,Local, CategoriaEventos
from django.views import generic
from drf_multiple_model.views import MultipleModelAPIView
from rest_framework import routers


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     TODO arreglar api para recuperar todo en un link
class LocalesViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all().filter(activo=True)
    serializer_class = LocalSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().filter(activo=True)
    serializer_class = EventSerializer

class CategoriaEventsViewSet(viewsets.ModelViewSet):
    queryset = CategoriaEventos.objects.all()
    serializer_class = CategoriaSerializer

class EventosView(generic.ListView):
    template_name = './events/eventos.html'
    context_object_name = 'locales_list'
    def get_queryset(self):
        return Local.objects.all().filter(activo=True)

class ApiViewTest(MultipleModelAPIView):
    objectify = True
    queryList = [(Local.objects.all().filter(activo=True),LocalSerializer),
                 (Evento.objects.all().filter(activo=True),EventSerializer)]