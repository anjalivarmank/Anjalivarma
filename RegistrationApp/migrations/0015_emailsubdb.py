# Generated by Django 4.1.2 on 2023-01-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0014_logindb'),
    ]

    operations = [
        migrations.CreateModel(
            name='emailsubdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
