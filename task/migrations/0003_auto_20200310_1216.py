# Generated by Django 3.0.3 on 2020-03-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(default='', max_length=200),
        ),
    ]