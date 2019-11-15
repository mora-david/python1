from rest_framework import viewsets
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializers


class EditorialViewSet(viewsets.ModelViewSet):
    """
    Editorial endpoint (viewset
    """
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializers