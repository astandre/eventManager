from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from events.models import Local, Evento
from events.serializers import LocalSerializer, EventSerializer
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


class LocalesList(generics.ListAPIView):
    """
        View for all Locales
    """

    queryset = Local.objects.filter(activo=True)
    serializer_class = LocalSerializer
    name = 'local-list'


class LocalesDetail(generics.RetrieveAPIView):
    """
    View for all locales detail
    """
    queryset = Local.objects.filter(activo=True).order_by('hora_inicio')
    serializer_class = LocalSerializer
    name = 'local-detail'


class EventosList(generics.ListAPIView):
    """
    View for all eventos
    """
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventSerializer
    name = 'evento-list'


class EventosDetail(generics.RetrieveAPIView):
    """
    View fro all eventos in detail
    """
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventSerializer
    name = 'evento-detail'


class EventosCategoriaFilter(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        cod_categoria = self.kwargs['cod_categoria']
        return Evento.objects.filter(nombre_categoria=cod_categoria)
