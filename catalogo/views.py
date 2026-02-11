from rest_framework import viewsets
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer
from rest_framework.permissions import IsAuthenticated

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticated]

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticated]