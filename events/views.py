from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from events.models import Local,Evento,CatEvento
from events.serializers import LocalSerializer,EventSerializer ,CategoriaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#     def get(self,request,*args,**kwargs):
#         return Response({
#             'eventos' : reverse(EventosList.name,request=request),
#             'locales' : reverse(LocalesList.name,request=request),
#
#         })
#

class LocalesList(generics.ListCreateAPIView):
    queryset = Local.objects.filter(activo=True)
    serializer_class = LocalSerializer
    name = 'local-list'

class LocalesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.filter(activo=True)
    serializer_class = LocalSerializer
    name = 'local-detail'


class CategoriasList(generics.ListCreateAPIView):
    queryset = CatEvento.objects.all()
    serializer_class = CategoriaSerializer
    name = 'catevento-list'

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatEvento.objects.all()
    serializer_class = CategoriaSerializer
    name = 'catevento-detail'

class EventosList(generics.ListCreateAPIView):
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventSerializer
    name = 'evento-list'

class EventosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventSerializer
    name = 'evento-detail'

#
# class JSONResponse(HttpResponse):
#     def __init__(self,data,**kwargs):
#         content = JSONRenderer().render(data)
#         kwargs["content_type"] = "application/json"
#         super(JSONResponse,self).__init__(content,**kwargs)
#
#
# @csrf_exempt
# def local_list(request):
#     if request.method == 'GET':
#         locales = Local.objects.all()
#         local_serializer = LocalSerializer(locales, many=True)
#         return JSONResponse(local_serializer.data)
#     return JSONResponse(LocalSerializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#
#
# @csrf_exempt
# def local_detail(request, pk):
#     try:
#         local = Local.objects.get(pk=pk)
#     except Local.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         local_serializer = LocalSerializer(local)
#         return JSONResponse(local_serializer.data)
#
#
# @csrf_exempt
# def event_list(request):
#     if request.method == 'GET':
#         events = Evento.objects.all()
#         events_serializer = EventSerializer(events, many=True)
#         return JSONResponse(events_serializer.data)
#     return JSONResponse(EventSerializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#
#
# @csrf_exempt
# def event_detail(request, pk):
#     try:
#         event = Evento.objects.get(pk=pk)
#     except Evento.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         events_serializer = EventSerializer(event)
#         return JSONResponse(events_serializer.data)
#
#
#
#
