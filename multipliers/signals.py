from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Multipliers


@receiver(post_migrate)
def create_Multipliers(sender, **kwargs):
    if Multipliers.objects.exists():
        return
    else:
        Multipliers.objects.create(
            multi_0_50=600,
            multi_51_150=300,
            multi_151_700=200,
            multi_701_1500=150,
            multi_1501_3000=85,
            multi_3001_6000=60,
            multi_6001_8=45,
        )
