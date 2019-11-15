from rest_framework import serializers
from editoriales.models import Editorial


class EditorialSerializers(serializers.ModelSerializer):
    """
    General purpose Editorial serializer
    """

    class Meta:
        model = Editorial
        fields = ('nombre', 'direccion', 'pagina_web', 'ciudad')
