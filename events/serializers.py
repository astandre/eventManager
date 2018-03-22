# from django.contrib.auth.serializers import User, Group

from rest_framework import serializers
from events.models import Evento, Local, CatEvento


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = (
            # 'url',
            # 'pk',
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


# class LocalEventoSerializer(serializers.HyperlinkedModelSerializer):
#     eventos = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='local-evento'
#     )
#
#     class Meta:
#         model = Local
#         fields = (
#             'url',
#             'pk',
#             # 'cod_local',
#             'nombre_local',
#             'activo',
#             'direccion_local',
#             'nombre_propietario',
#             'telefono_local',
#             'celular_local',
#             'email_local'
#         )

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatEvento
        fields = (
            'cod_categoria',
            'nombre_categoria',

        )


class EventSerializer(serializers.HyperlinkedModelSerializer):

    # local= serializers.SlugRelatedField(queryset=Local.objects.all(),
    #                                     slug_field="nombre_local")
    # local = LocalSerializer(many=True, read_only=True)
    categorias_eventos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
            'categorias_eventos'
        )

# cod_evento = serializers.IntegerField(read_only=True)
# nombre_evento = serializers.CharField(max_length=30)
# descripcion_evento = serializers.CharField(max_length=200)
# activo = serializers.BooleanField(default=True)
# familiar = serializers.BooleanField(default=True)
# hora_inicio = serializers.DateTimeField()
# hora_fin = serializers.DateTimeField()
# img = serializers.CharField(max_length=300)
# # local = serializers. (Local, on_delete=serializers.CASCADE)
#
# def create(self,validated_data):
#     return Evento.objects.create(**validated_data)
#
# def update(self, instance, validated_data):
#     instance.nombre_evento = validated_data.get('nombre_evento',instance.nombre_evento)
#     instance.save()
#     return instance
#
