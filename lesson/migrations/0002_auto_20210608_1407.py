# Generated by Django 3.2.4 on 2021-06-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='intro',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='lesson',
            name='videoURL',
            field=models.CharField(default='', max_length=100),
        ),
    ]
