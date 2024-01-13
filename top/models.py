from django.db import models
from django.contrib.auth.models import User

class ClassData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    metadata = models.TextField()
