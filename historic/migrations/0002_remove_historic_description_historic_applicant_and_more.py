# Generated by Django 4.1.7 on 2023-05-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("historic", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historic",
            name="description",
        ),
        migrations.AddField(
            model_name="historic",
            name="applicant",
            field=models.CharField(default="Not specified", max_length=40),
        ),
        migrations.AddField(
            model_name="historic",
            name="client",
            field=models.CharField(default="Not specified", max_length=40),
        ),
    ]