# Generated by Django 4.1.2 on 2022-12-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0008_add_admindb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('discription', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
        migrations.DeleteModel(
            name='add_studentdb',
        ),
    ]
