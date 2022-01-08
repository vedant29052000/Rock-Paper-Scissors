from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


class UserName(models.Model):
    Username = models.CharField(max_length=60)
    class Meta:
        db_table = "Users"