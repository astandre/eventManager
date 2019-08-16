from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Local, Evento, Direccion
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from django.db.models import F
from .serializers import *


# def index(request):
#     """
#     View of the main page
#     """
#     return render(request, 'Index.html')


# def handler404(request):
#     response = render_to_response('404.html')
#     response.status_code = 404
#     return response


@api_view(['GET'])
def eventos_api(request):
    if request.method == 'GET':
        eventos = list(
            Evento.objects.annotate(id_local=F('local__id_local')).values("id_local", "nombre", "descripcion",
                                                                          "familiar", "direccion",
                                                                          "fecha_inicio", "fecha_fin", "image",
                                                                          "categoria", "id_evento").filter(activo=True))

        return JsonResponse({"eventos": eventos}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"Error": "Only GET is Allowed"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def eventos_categoria_api(request, categoria):
    if request.method == 'GET':
        categoria = categoria.upper()
        if categoria in Evento.CATEGORIAS:
            eventos = list(
                Evento.objects.annotate(id_local=F('local__id_local')).values("id_local", "nombre", "descripcion",
                                                                              "familiar", "direccion",
                                                                              "fecha_inicio", "fecha_fin", "image",
                                                                              "categoria", "id_evento").filter(
                    categoria=categoria, activo=True))
            return JsonResponse({"eventos": eventos}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"eventos": "Categoria de evento no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({"Error": "Only GET is Allowed"}, status=status.HTTP_403_FORBIDDEN)
