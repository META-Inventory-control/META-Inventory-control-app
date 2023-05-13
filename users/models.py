from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_operator = models.BooleanField(default=False)
