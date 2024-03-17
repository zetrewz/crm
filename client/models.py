from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

# User = get_user_model()
#
#
# class Client(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name='clients')
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     company_name = models.CharField(max_length=255)
#
#
