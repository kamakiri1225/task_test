# Generated by Django 3.0.11 on 2021-01-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210119_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='question_num',
        ),
        migrations.AddField(
            model_name='choise',
            name='question_num',
            field=models.IntegerField(default=0),
        ),
    ]