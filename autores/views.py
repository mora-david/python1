from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from autores.models import Autor
from autores.serializers import AutorSerializer
from rest_framework.decorators import action
from Libros.models import Libro
from Libros.serializers import LibroSerializer


class AutorViewSet(viewsets.ModelViewSet):
    """
    Autor endpoint (ViewSet)
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None):
        autor = self.get_object()
        libros = Libro.objects.filter(autores__id=autor.id)
        serialized = LibroSerializer(libros, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
