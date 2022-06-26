from rest_framework import serializers
from notebookapi.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('__all__')
        depth = 3

class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'body', 'tags', 'datetime', 'user_id']