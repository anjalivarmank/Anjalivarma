# Generated by Django 4.1.2 on 2022-12-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0004_alter_add_bookdb_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_studentdb',
            name='Book',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]