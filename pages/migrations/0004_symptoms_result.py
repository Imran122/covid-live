# Generated by Django 3.1.1 on 2020-10-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_symptoms_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptoms',
            name='result',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
