# Generated by Django 5.0.2 on 2024-04-05 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_cardname_card_card_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_id',
            new_name='cardName',
        ),
    ]
