# Generated by Django 4.1.2 on 2023-01-05 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0016_messagedb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Products',
            old_name='category',
            new_name='bcategory',
        ),
        migrations.RenameField(
            model_name='Categorydb',
            old_name='name',
            new_name='cname',
        ),
    ]
