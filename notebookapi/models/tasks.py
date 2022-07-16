from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    datetime = models.CharField(max_length=500)
    user_id = models.ForeignKey("NoteTaker", on_delete=models.CASCADE)