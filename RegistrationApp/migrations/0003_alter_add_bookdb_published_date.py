# Generated by Django 4.1.2 on 2022-11-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0002_add_bookdb_alter_add_studentdb_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Products',
            name='Published_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]