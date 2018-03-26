from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from events.models import Local, Evento, CatEvento
from events.serializers import LocalSerializer, EventSerializer, CategoriaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    """
    View of the main page
    """
    return render(request, 'Index.html')


def handler404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


class LocalesList(generics.ListCreateAPIView):
    """
        View for all Locales
    """

    queryset = Local.objects.filter(activo=True)
    serializer_class = LocalSerializer
    name = 'local-list'


class LocalesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for all locales detail
    """
    queryset = Local.objects.filter(activo=True).order_by('hora_inicio')
    serializer_class = LocalSerializer
    name = 'local-detail'


class CategoriasList(generics.ListCreateAPIView):
    """
    View for all Categorias
    """
    queryset = CatEvento.objects.all()
    serializer_class = CategoriaSerializer
    name = 'catevento-list'


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for all Categorias in detail
    """
    queryset = CatEvento.objects.all()
    serializer_class = CategoriaSerializer
    name = 'catevento-detail'


class EventosList(generics.ListCreateAPIView):
    """
    View for all eventos
    """
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventSerializer
    name = 'evento-list'


class EventosDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View fro all eventos in detail
    """
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventSerializer
    name = 'evento-detail'
