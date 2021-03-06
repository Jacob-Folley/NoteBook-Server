from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    tags = models.CharField(max_length=12, blank=True)
    datetime = models.CharField(max_length=500)
    user_id = models.ForeignKey("NoteTaker", on_delete=models.CASCADE)