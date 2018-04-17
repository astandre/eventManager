# from django.contrib.auth.serializers import User, Group

from rest_framework import serializers
from events.models import Evento, Local


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = (
            'cod_local',
            'nombre_local',
            'img_local',
            'direccion_local',
            'latitud_local',
            'longitud_local',
            'nombre_propietario',
            'telefono_local',
            'celular_local',
            'email_local'
        )


class EventSerializer(serializers.HyperlinkedModelSerializer):
    # local= serializers.SlugRelatedField(queryset=Local.objects.all(),
    #                                     slug_field="nombre_local")
    # local = LocalSerializer(many=True, read_only=True)
    # categorias_eventos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    local = LocalSerializer(read_only=True)

    # categorias_eventos = CategoriaSerializer(many=True, read_only=True)
    class Meta:
        model = Evento
        fields = (
            # 'url',
            # 'direccion',
            'cod_evento',
            'nombre_evento',
            'descripcion_evento',
            'familiar',
            'fecha_inicio',
            'direccion_evento',
            'latitud_evento',
            'longitud_evento',
            'fecha_fin',
            'img',
            'local',
        )
