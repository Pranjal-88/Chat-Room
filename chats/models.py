from django.db import models
from datetime import date, datetime

class Room(models.Model):
    name=models.CharField(max_length=200)

class Message(models.Model):
    content=models.CharField(max_length=10000)
    time=models.TimeField(default=datetime.now().time())
    user=models.CharField(max_length=200)
    room_id=models.CharField(max_length=200)

