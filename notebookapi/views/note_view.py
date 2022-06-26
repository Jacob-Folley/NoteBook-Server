from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from notebookapi.serializers import NoteSerializer, NoteCreateSerializer
from notebookapi.models import Note


class NoteView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single Note
        Returns:
            Response -- JSON serialized game type"""
        try:
            note = Note.objects.get(pk=pk)
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        except Note.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all Note
        Returns:
            Response -- JSON serialized list of game types"""
        note = Note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to Note"""
        serializer = NoteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Note"""
        try:
            note = Note.objects.get(pk=pk)
            serializer = NoteCreateSerializer(note, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Note"""
        note = Note.objects.get(pk=pk)
        note.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)