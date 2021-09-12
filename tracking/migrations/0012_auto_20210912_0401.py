# Generated by Django 3.2.4 on 2021-09-12 02:01

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0011_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='my_address',
            field=models.CharField(default='qina', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='my_location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True),
        ),
    ]
