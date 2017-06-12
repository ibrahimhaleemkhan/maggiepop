from __future__ import unicode_literals
import uuid
from django.contrib.auth.models import User




# Create your models here.
from django.db import models



class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    REQUIRED_FIELDS = ('user',)
    latitude=models.CharField(max_length=40)
    longitude=models.CharField(max_length=40)


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host=models.ForeignKey(User)
    type=models.IntegerField()
    latitude=models.CharField(max_length=40)
    longitude=models.CharField(max_length=40)
    participants = models.ManyToManyField(User, related_name='participants')



