# Generated by Django 4.1.2 on 2023-01-05 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0018_rename_bcategory_add_bookdb_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Products',
            old_name='name',
            new_name='bname',
        ),
        migrations.RenameField(
            model_name='Categorydb',
            old_name='name',
            new_name='cname',
        ),
    ]
