# Generated by Django 3.2.3 on 2021-06-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('DONE', 'Done'), ('NOT DONE', 'Not done')], default='Not done', max_length=20),
        ),
    ]