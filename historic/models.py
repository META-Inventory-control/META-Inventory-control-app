from django.db import models
import uuid


# Create your models here.
class Historic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.CharField(null=False, max_length=100)
    qty = models.IntegerField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
