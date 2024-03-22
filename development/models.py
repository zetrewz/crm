from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, SET_NULL

User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=255)
    head = models.ForeignKey(User, on_delete=CASCADE, related_name='projects')

    # def __str__(self):
    #     return self.name


class Team(models.Model):
    lead = models.ForeignKey(
        User,
        on_delete=SET_NULL,
        related_name='my_team',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project,
        on_delete=SET_NULL,
        related_name='teams',
        null=True,
        blank=True
    )

    # def __str__(self):
    #     return self.name


class Sprint(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(
        Team,
        on_delete=CASCADE,
        related_name='sprints'
    )
    started = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project,
        on_delete=CASCADE,
        related_name='tasks'
    )
    sprint = models.ForeignKey(
        Sprint,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    created = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name


class Invitation(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='invitations')
    team = models.ForeignKey(Team, on_delete=CASCADE, related_name='invitations')
