from rest_framework import serializers
from API.models import Usuario

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'