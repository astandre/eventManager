from django.contrib.auth.models import User, Group

from rest_framework import serializers
from events.models import Evento,Local, CategoriaEventos
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEventos
        fields = '__all__'



