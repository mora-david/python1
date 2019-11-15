from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from Libros.serializers import LibroSerializer, CreateLibroSerializer
from Libros.models import Libro
from autores.serializers import AutorSerializer
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializers



class LibroViewSet(viewsets.ModelViewSet):
    """
    Libro endpoint (viewset)
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLibroSerializer
        return LibroSerializer

    @action(detail=True, methods=['GET'])
    def autores(self, request, pk=None):
        libro = self.get_object()
        serialized = AutorSerializer(libro.autores, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def editorial(self, request, pk=None):
        libro = self.get_object()
        serialized = EditorialSerializers(libro.editorial)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
