from rest_framework.serializers import ModelSerializer
from .models import Please


class PleaseSerializer(ModelSerializer):

    class Meta:
        model = Please
        fields = ['emailplus', 'country', 'phone_number']
