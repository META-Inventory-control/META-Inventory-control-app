from django.db import models
import uuid


# Create your models here.
class Multipliers(models.Model):
    ###id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    multi_0_50 = models.IntegerField()
    multi_51_150 = models.IntegerField()
    multi_151_700 = models.IntegerField()
    multi_701_1500 = models.IntegerField()
    multi_1501_3000 = models.IntegerField()
    multi_3001_6000 = models.IntegerField()
    multi_6001_8 = models.IntegerField()
