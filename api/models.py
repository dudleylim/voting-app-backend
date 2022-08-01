from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Candidate(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + ' ' + self.candidate.name