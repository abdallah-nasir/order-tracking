# Generated by Django 3.2.4 on 2021-09-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ManyToManyField(to='tracking.Shop'),
        ),
    ]