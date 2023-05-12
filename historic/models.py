from django.db import models
import uuid


# Create your models here.
class Historic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    client = models.CharField(null=False, max_length=40, default="Not specified")
    applicant = models.CharField(null=False, max_length=40, default="Not specified")
    qty = models.IntegerField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
