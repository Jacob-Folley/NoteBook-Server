from rest_framework import serializers
from notebookapi.models import NoteTaker


class NoteTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTaker
        fields = ('__all__')
        depth = 3

class NoteTakerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTaker
        fields = ['user', 'bio']