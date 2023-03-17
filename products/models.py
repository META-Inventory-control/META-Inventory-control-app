from django.db import models
import uuid


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(null=False, max_length=100)
    entry_cost = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    final_cost = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    qty = models.IntegerField(null=False)
    image = models.ImageField(null=True, max_length=30)
