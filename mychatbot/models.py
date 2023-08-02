from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class Conversation(models.Model):
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"

class ChatRequestCounter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    count = models.PositiveIntegerField(default=0)