# Generated by Django 4.1.7 on 2023-04-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="code",
            field=models.CharField(default="Nocode", editable=False, max_length=7),
            preserve_default=False,
        ),
    ]
