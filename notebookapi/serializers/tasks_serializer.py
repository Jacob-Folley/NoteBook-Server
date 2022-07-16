from rest_framework import serializers
from notebookapi.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('__all__')
        depth = 3

class TasksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['title', 'body', 'datetime', 'user_id']