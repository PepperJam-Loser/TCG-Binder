# Generated by Django 5.0.2 on 2024-03-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastCardIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_index', models.IntegerField(default=0)),
            ],
        ),
    ]