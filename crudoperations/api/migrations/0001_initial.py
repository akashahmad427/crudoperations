# Generated by Django 4.1.7 on 2023-06-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('roll', models.IntegerField(max_length=70)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]