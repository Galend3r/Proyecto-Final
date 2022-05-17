from django.db import models

class Message(models.Model):
    from_message = models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    