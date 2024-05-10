# Generated by Django 5.0.2 on 2024-05-09 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_deck_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='visibility',
        ),
        migrations.AddField(
            model_name='deck',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
