from django.db import models
from django.contrib.auth.models import User

class ChatLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.created_at} - {self.user.username}"

