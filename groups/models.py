from django.db import models

# Create your models here.
from django.db import models
import uuid


# Create your models here.
class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    group_name = models.CharField(null=False, max_length=100)
