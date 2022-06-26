from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=55)
    body = models.CharField(max_length=10000)
    tags = models.CharField(max_length=12)
    datetime = models.DateTimeField()
    user_id = models.ForeignKey("NoteTaker", on_delete=models.CASCADE)