from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from notebookapi.serializers import NoteTakerSerializer, NoteTakerCreateSerializer
from notebookapi.models import NoteTaker


class NoteTakerView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single NoteTaker
        Returns:
            Response -- JSON serialized game type"""
        try:
            notetaker = NoteTaker.objects.get(pk=pk)
            serializer = NoteTakerSerializer(notetaker)
            return Response(serializer.data)
        except NoteTaker.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all NoteTaker
        Returns:
            Response -- JSON serialized list of game types"""
        note = NoteTaker.objects.all()
        serializer = NoteTakerSerializer(note, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to NoteTaker"""
        serializer = NoteTakerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update NoteTaker"""
        try:
            notetaker = NoteTaker.objects.get(pk=pk)
            serializer = NoteTakerCreateSerializer(notetaker, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except NoteTaker.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete NoteTaker"""
        notetaker = NoteTaker.objects.get(pk=pk)
        notetaker.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)