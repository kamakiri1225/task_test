# Generated by Django 3.0.11 on 2021-01-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='question_text',
            new_name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='question_num',
            field=models.IntegerField(default=0),
        ),
    ]