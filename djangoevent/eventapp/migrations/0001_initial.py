# Generated by Django 5.1.1 on 2024-09-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='uploads')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=100)),
            ],
        ),
    ]
