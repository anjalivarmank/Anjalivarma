# Generated by Django 4.1.2 on 2023-01-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontapp', '0005_remove_cartdb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cartdb',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
