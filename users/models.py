from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL


class User(AbstractUser):
    team = models.ForeignKey(
        'development.Team',
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )
