from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from notebookapi.serializers import TasksSerializer, TasksCreateSerializer
from notebookapi.models import Tasks


class TasksView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single Tasks
        Returns:
            Response -- JSON serialized game type"""
        try:
            tasks = Tasks.objects.get(pk=pk)
            serializer = TasksSerializer(tasks)
            return Response(serializer.data)
        except Tasks.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Tasks
        Returns:
            Response -- JSON serialized list of game types"""
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to Tasks"""
        serializer = TasksCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Tasks"""
        try:
            tasks = Tasks.objects.get(pk=pk)
            serializer = TasksCreateSerializer(tasks, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tasks.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Tasks"""
        tasks = Tasks.objects.get(pk=pk)
        tasks.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)