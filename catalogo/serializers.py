from rest_framework import serializers
from .models import Autor, Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    libros = LibroSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = '__all__'
