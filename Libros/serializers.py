from rest_framework import serializers
from Libros.models import Libro
from editoriales.serializers import EditorialSerializers
from autores.serializers import AutorSerializer


class LibroSerializer(serializers.ModelSerializer):
    """
    General purpose Libro serializer
    """
    autores = AutorSerializer(many=True)
    editorial = EditorialSerializers()

    class Meta:
        model = Libro
        fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')


class CreateLibroSerializer(serializers.ModelSerializer):
    """
    Create Libro serializer whitout related fields
    """
    class Meta:
        model = Libro
        fields = ('titulo', 'autores', 'editorial', 'fecha_publicacion')