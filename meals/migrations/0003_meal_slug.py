# Generated by Django 2.2 on 2020-04-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20200423_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]