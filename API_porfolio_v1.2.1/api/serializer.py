from rest_framework import serializers
from .models import Programer

class ProgramerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Programer
        fields = '__all__' #para que se serializen todos los campos
        #fields = ('id', 'fullname', 'nickname') serializa tales campos en espesifico.