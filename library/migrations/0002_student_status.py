# Generated by Django 5.1 on 2024-08-28 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='Active', max_length=10),
        ),
    ]
